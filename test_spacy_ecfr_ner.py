from spacy.cli.project.run import project_run
#from spacy.cli.project.assets import project_assets
from pathlib import Path


def test_spacy_ecfr_ner():
    root = Path(__file__).parent
    project_run(root, "all", capture=True)

