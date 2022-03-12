"""Convert NER annotation from JSONL to spaCy v3 .spacy format."""
import srsly
import typer
from pathlib import Path
from rich.console import Console
from spacy.util import get_words_and_spaces
from spacy.tokens import Doc, DocBin
import spacy


def convert_ner(
    lang: str, 
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(..., dir_okay=False),
):
    nlp = spacy.blank(lang)
    console = Console()

    doc_bin = DocBin(attrs=["ENT_IOB", "ENT_TYPE"])
    for eg in srsly.read_jsonl(input_path):
        if eg["answer"] != "accept":
            continue
        tokens = [token["text"] for token in eg["tokens"]]
        words, spaces = get_words_and_spaces(tokens, eg["text"])
        doc = Doc(nlp.vocab, words=words, spaces=spaces)
        doc.ents = [
            doc.char_span(s["start"], s["end"], label=s["label"])
            for s in eg.get("spans", [])
        ]
        doc_bin.add(doc)
    doc_bin.to_disk(output_path)
    console.log(f"spacy file written at {output_path}")

if __name__ == "__main__":
    typer.run(convert_ner)
