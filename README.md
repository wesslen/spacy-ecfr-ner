<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: NER Citations of ECFR Banking Regulation in a spaCy pipeline.

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
| `data-to-spacy` | Merge your annotations and create data in spaCy's binary format |
| `data-to-asset-senter` | Export senter annotations to assets |
| `train-curve-ner` | Train curve for NER |
| `data-to-asset-ner` | Export NER annotations to assets |
| `train` | Train pipeline models |
| `evaluate` | Evaluate the model and export metrics |
| `prodigy-al-ner` | NER prodigy active learning annotaitons |
| `prodigy-manual-ner` | NER prodigy manual learning annotations |
| `package` | Package the trained model as a pip package |
| `visualize-model` | Visualize the model's output interactively using Streamlit |
| `setup` | Install dependencies |
| `clean` | Remove intermediate files |
| `document` | Export README for project details |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `download` &rarr; `train` &rarr; `evaluate` &rarr; `package` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/ecfr_ner_labels.jsonl`](assets/ecfr_ner_labels.jsonl) | Local | 400 initial NER labels of sections, cites, and laws |
| [`assets/patterns.jsonl`](assets/patterns.jsonl) | Local | Patterns for sections, cites, and laws for initial NER training |
| [`assets/ecfr_senter_labels.jsonl`](assets/ecfr_senter_labels.jsonl) | Local | 150 initial sentence segmentations of eCFR sub-sections |
| [`assets/raw-files/ecfr-sample-sents.jsonl`](assets/raw-files/ecfr-sample-sents.jsonl) | Local | Sample of Prodigy annotated sentences from ecfr-sample-title-12.jsonl file |
| [`assets/raw-files/ecfr-sample-title-12.jsonl`](assets/raw-files/ecfr-sample-title-12.jsonl) | Local | Sample of 47 records (sub-sections) from ecfr-title-12.jsonl |
| [`assets/raw-files/ecfr-title-12.jsonl`](assets/raw-files/ecfr-title-12.jsonl) | Local | eCFR Title 12 (Banking) parsed as a jsonl file |
| [`assets/raw-files/ecfr-title-12-sent.jsonl`](assets/raw-files/ecfr-title-12-sent.jsonl) | Local | Senter scored model segmenting ecfr-title-12.jsonl |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
