import srsly
import typer
import random
from pathlib import Path

def main(input_loc: Path, output_loc: Path):
    """Shuffle jsonl."""

    # "./assets/ecfr-title-12.jsonl"
    examples = srsly.read_jsonl(input_loc)

    random.shuffle(list(examples))
    # "./assets/ecfr-title-12-sent.jsonl"
    srsly.write_jsonl(output_loc, examples)

if __name__ == "__main__":
    typer.run(main)