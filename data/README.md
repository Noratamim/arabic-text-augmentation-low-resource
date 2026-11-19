# Dataset handling

Place the extracted upstream ASTD repository under `data/raw/ASTD-master/`. Do not commit the raw tweet file or generated processed splits unless redistribution terms have been explicitly checked and approved.

Expected source files:
- `data/raw/ASTD-master/data/Tweets.txt`
- `data/raw/ASTD-master/data/4class-unbalanced-train.txt`
- `data/raw/ASTD-master/data/4class-unbalanced-validation.txt`
- `data/raw/ASTD-master/data/4class-unbalanced-test.txt`

See the repository README and `notebooks/00_dataset_audit.ipynb` for source, citation, label mapping, and duplicate/leakage checks.
