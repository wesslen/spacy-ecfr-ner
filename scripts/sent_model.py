import spacy
import srsly
import typer
import random
from pathlib import Path

def main(model_loc: Path, sample_loc: Path, output_loc: Path):
    """Create sentence jsonl annotations."""

    # "senter/model-last"
    nlp = spacy.load(model_loc)
    # "./assets/ecfr-title-12.jsonl"
    examples = srsly.read_jsonl(sample_loc)

    texts = (eg["text"] for eg in examples)
    #meta = (eg["meta"] for eg in examples)

    new_examples = []
    for doc in nlp.pipe(texts):
        # create enumerate; assign meta for each doc by index
        #m = next(meta)
        
        for sent in doc.sents:
            new_examples.append({"text": sent.text}) # , "meta": m

    random.shuffle(new_examples)
    # "./assets/ecfr-title-12-sent.jsonl"
    srsly.write_jsonl(output_loc, new_examples)

if __name__ == "__main__":
    typer.run(main)