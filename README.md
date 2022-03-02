<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: NER on ECFR Banking Regulation in a new pipeline (Named Entity Recognition)

Custom NER project for spaCy v3 adapted from the spaCy v3 [`ner_demo`](https://github.com/explosion/projects/tree/9d5fce5f95ddf5f35c3370b2074b25e995525f51/pipelines/ner_demo) example script for creating an NER component in a new pipeline.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `download` | Download a spaCy model with pretrained vectors |
| `train-senter` | Train a custom sentence/parser for ECFR |
| `convert` | Convert the data to spaCy's binary format |
| `create-config` | Create a new config with an NER pipeline component |
| `train` | Train the NER model |
| `train-with-vectors` | Train the NER model with vectors |
| `evaluate` | Evaluate the model and export metrics |
| `visualize-model` | Visualize the model's output interactively using Streamlit |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `convert` &rarr; `create-config` &rarr; `train-senter` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/train.json` | Local | Demo training data converted from the v2 `train_ner.py` example with `srsly.write_json("train.json", TRAIN_DATA)` |
| `assets/dev.json` | Local | Demo development data |
| `assets/ecfr-sample_sents.jsonl` | Local | Gold-standard REL annotations created with Prodigy |
| [`assets/ecfr-sample-sents.jsonl`](assets/ecfr-sample-sents.jsonl) | Local | Sample sentences of ECFR labeled with Prodigy |
| [`assets/sample-ecfr12.jsonl`](assets/sample-ecfr12.jsonl) | Local | 1% sample sentences for Sentence Segmenter |
| [`assets/patterns.jsonl`](assets/patterns.jsonl) | Local | Patterns for sections, cites, and laws for NER training |
| [`assets/ecfr-title-12.jsonl`](assets/ecfr-title-12.jsonl) | Local | Full ECFR 12 by section |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
