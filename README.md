# Arabic Text Augmentation for Low-Resource Classification

**Project question:** Compare Back-Translation, Masked Language Model (MLM) augmentation, and Controlled Generation for Arabic text classification under low-resource training conditions, using an untouched, human-annotated test set.

> Project repository for CS 0613 — Selected Topic in Applied Artificial Intelligence.

## Current status

- [x] ASTD archive received and inspected.
- [x] Verified four source labels and official 6:2:2 unbalanced split files.
- [x] Identified exact duplicate texts crossing the supplied train/validation/test partitions; the audit notebook documents a safe handling rule that preserves the original test rows.
- [ ] Confirm dataset choice and final split protocol with the project team/instructor.
- [ ] Run baseline without augmentation.
- [ ] Run Back-Translation, MLM, and Controlled Generation experiments.
- [ ] Complete statistical analysis, error analysis, IEEE report, and presentation.

## Repository layout

```text
.
├── data/
│   ├── raw/              # Local source dataset (ignored by Git)
│   └── processed/        # Generated clean splits (ignored by Git)
├── docs/                # Project decisions and student work plan
├── notebooks/           # Jupyter notebooks
├── references/          # BibTeX and source notes
├── reports/             # Audit summaries and figures
└── src/                 # Reusable project code
```

## Dataset setup (ASTD)

The current candidate dataset is ASTD (Arabic Sentiment Tweets Dataset), introduced by Nabil, Aly, and Atiya at EMNLP 2015. The original paper describes 10,006 Arabic tweets in four categories: objective, subjective positive, subjective negative, and subjective mixed. It reports that the labels were assigned using three human raters; examples with agreement from at least two raters were retained.

1. Download the upstream repository: <https://github.com/mahmoudnabil/ASTD>
2. Extract it locally so this file exists: `data/raw/ASTD-master/data/Tweets.txt`
3. Keep the upstream files local. This repository intentionally ignores raw and processed dataset files until the exact redistribution terms are confirmed. The upstream repository includes a GPL-2.0 license file; do not assume it automatically resolves every right associated with underlying social-media text.
4. Open `notebooks/00_dataset_audit.ipynb` and run all cells.

The original paper is available at <https://aclanthology.org/D15-1299/> and DOI <https://doi.org/10.18653/v1/D15-1299>. Cite the dataset paper in every report/publication that uses ASTD.

### Labels in the uploaded text file

The actual labels in `Tweets.txt` are `POS`, `NEG`, `NEUTRAL`, and `OBJ`. The original paper describes the four semantic classes as subjective positive, subjective negative, subjective mixed, and objective. The repository's `NEUTRAL` code corresponds to the original paper's mixed category; preserve the raw label and document this mapping explicitly.

### Preliminary audit of the uploaded archive

| Label code | Meaning in the original paper | Records | Share |
|---|---|---:|---:|
| `OBJ` | Objective | 6,691 | 66.87% |
| `NEG` | Subjective negative | 1,684 | 16.83% |
| `NEUTRAL` | Subjective mixed | 832 | 8.32% |
| `POS` | Subjective positive | 799 | 7.99% |
| **Total** | | **10,006** | **100%** |

The upstream unbalanced split files contain 6,008 training, 1,999 validation, and 1,999 test IDs. The ID partitions are mutually exclusive and cover all 10,006 records. After trimming leading/trailing whitespace, the uploaded `Tweets.txt` contains five exact-duplicate text groups (five extra rows); four duplicate groups cross the supplied train/validation/test boundaries and one duplicate group occurs twice within training. The audit notebook keeps the official test rows unchanged and removes duplicate copies from training/validation to prevent exact-text leakage. Confirm this handling with the team before finalizing the experimental protocol.

## Environment setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Reproducibility principles

- Keep the same data split, classification model, preprocessing, and training settings across augmentation experiments.
- Apply augmentation to training data only.
- Never use the test set for augmentation, hyperparameter selection, or model selection.
- Report Macro-F1 alongside Accuracy because the source dataset is strongly imbalanced.
- Record random seeds, dataset version, model checkpoint, and package versions.
- Do not publish private credentials, API keys, or raw user-identifying information.

## Core research paper candidate

Mayaleh, M. S., & Mayaleh, S. A. (2026). *Enhancing sentiment classification on small datasets through data augmentation and transfer learning*. Discover Artificial Intelligence, 6, 127. https://doi.org/10.1007/s44163-025-00813-9

This paper is a candidate core paper because it is an original empirical study and compares EDA, back-translation, and contextual substitution on a small sentiment dataset. However, it uses English IMDb data and does not test controlled LLM generation; our proposed extension is Arabic data plus the three methods required by the project.
