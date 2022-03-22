import srsly
import typer
import streamlit as st
from typing import List, Sequence, Optional, Dict, Union
import spacy
import pandas as pd

from spacy import displacy

import base64


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model(name: str) -> spacy.language.Language:
    """Load a spaCy model."""
    return spacy.load(name)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def process_text(model_name: str, text: str) -> spacy.tokens.Doc:
    """Process a text and create a Doc object."""
    nlp = load_model(model_name)
    return nlp(text)


def get_svg(svg: str, style: str = "", wrap: bool = True):
    """Convert an SVG to a base64-encoded image."""
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" style="{style}"/>'
    return get_html(html) if wrap else html


def get_html(html: str):
    """Convert HTML so it can be rendered."""
    WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
    # Newlines seem to mess with the rendering
    html = html.replace("\n", " ")
    return WRAPPER.format(html)

def get_json(sample_loc: str):
    """Get sample of records"""
    examples = srsly.read_jsonl(sample_loc)
    texts = (eg["text"] for eg in examples)
    return list(texts)


def visualize_nerparser(
    doc: spacy.tokens.Doc,
    *,
    title: Optional[str] = "Sentence segmentation and NER",
) -> None:
    if title:
        st.header(title)

    docs = [span.as_doc() for span in doc.sents]
    for sent in docs:
        
        labels = [ent.label_ for ent in sent.ents]
        # Double newlines seem to mess with the rendering
        #displacy_options["ents"] = label_select
        html = displacy.render(
            sent,
            style="ent",
            #options=displacy_options,
            #manual=manual,
        )
        style = "<style>mark.entity { display: inline-block }</style>"
        st.write(f"{style}{get_html(html)}", unsafe_allow_html=True)


def main(models: str):
    st.title("eCFR Title 12 NER+Segmenter")
    models = [name.strip() for name in models.split(",")]
    default_text = "This subpart prescribes uniform rules of practice and procedure applicable to adjudicatory proceedings required to be conducted on the record after opportunity for a hearing under the following statutory provisions:, (a) Cease-and-desist proceedings under section 206(e) of the Act (12 U.S.C. 1786(e));, (b) Removal and prohibition proceedings under section 206(g) of the Act (12 U.S.C. 1786(g));, (c) Assessment of civil money penalties by the NCUA Board against institutions and institution-affiliated parties for any violation of:, (1) Section 202 of the Act (12 U.S.C. 1782);, (2) Section 1120 of FIRREA (12 U.S.C. 3349), or any order or regulation issued thereunder; , (3) The terms of any final or temporary order issued under section 206 of the Act or any written agreement executed by the National Credit Union Administration (\u201cNCUA\u201d), any condition imposed in writing by the NCUA in connection with any action on any application, notice, or other request by the credit union or institution-affiliated party, certain unsafe or unsound practices or breaches of fiduciary duty, or any law or regulation not otherwise provided herein, pursuant to 12 U.S.C. 1786(k); and, (4) Any provision of law referenced in section 102(f) of the Flood Disaster Protection Act of 1973 (42 U.S.C. 4012a(f)) or any order or regulation issued thereunder;, (d) Remedial action under section 102(g) of the Flood Disaster Protection Act of 1973 (42 U.S.C. 4012a(g)); and, (e) This subpart also applies to all other adjudications required by statute to be determined on the record after opportunity for an agency hearing, unless otherwise specifically provided for in subparts B through J of this part."
    
    input_model = st.sidebar.selectbox(label="Choose model", options=models)
    check = st.sidebar.checkbox(label="Custom input or not",value=True)
    texts = get_json("assets/raw-files/ecfr-sample-title-12.jsonl")
    if check:
        input_text = st.text_area(label="Input eCFR sub-section", value=default_text, height = 100)  
    else:
        input_slider = st.sidebar.slider("Sample text", min_value=0,max_value=46)
        input_text = texts[input_slider]
        st.write(input_text)
    doc = process_text(input_model, input_text)
    visualize_nerparser(doc)
    #spacy_streamlit.visualize(models, default_text, visualizers=["parser","ner"])


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass
