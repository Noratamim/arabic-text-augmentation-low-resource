from __future__ import annotations

from pathlib import Path
import pandas as pd

LABEL_MEANING = {
    "POS": "Subjective positive",
    "NEG": "Subjective negative",
    "NEUTRAL": "Subjective mixed (label code used in the uploaded file)",
    "OBJ": "Objective",
}


def load_astd(data_dir: str | Path) -> pd.DataFrame:
    """Load ASTD Tweets.txt (one Arabic tweet and one label per tab-separated row)."""
    data_dir = Path(data_dir)
    tweets_file = data_dir / "Tweets.txt"
    if not tweets_file.exists():
        raise FileNotFoundError(
            f"Could not find {tweets_file}. Extract ASTD-master under data/raw/ first."
        )

    rows: list[dict[str, str | int]] = []
    with tweets_file.open("r", encoding="utf-8") as f:
        for row_id, raw_line in enumerate(f):
            line = raw_line.rstrip("\r\n")
            if "\t" not in line:
                raise ValueError(f"Row {row_id} has no tab separator: {line[:80]!r}")
            text, label = line.rsplit("\t", 1)
            rows.append({"row_id": row_id, "text": text.strip(), "label": label.strip()})

    df = pd.DataFrame(rows)
    unexpected = sorted(set(df["label"]) - set(LABEL_MEANING))
    if unexpected:
        raise ValueError(f"Unexpected labels found: {unexpected}")
    if df["text"].eq("").any():
        raise ValueError("Empty tweet text found; inspect source rows before proceeding.")
    return df


def load_official_unbalanced_splits(data_dir: str | Path, df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Read the official unbalanced split ID files (IDs are zero-based row positions)."""
    data_dir = Path(data_dir)
    splits: dict[str, pd.DataFrame] = {}
    for split in ("train", "validation", "test"):
        path = data_dir / f"4class-unbalanced-{split}.txt"
        if not path.exists():
            raise FileNotFoundError(f"Missing official split file: {path}")
        ids = [int(x.strip()) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
        if len(ids) != len(set(ids)):
            raise ValueError(f"Duplicate row IDs inside {split} split file.")
        if any(i < 0 or i >= len(df) for i in ids):
            raise ValueError(f"Out-of-range row ID found in {split} split.")
        splits[split] = df.iloc[ids].copy().reset_index(drop=True)
    return splits


def remove_exact_duplicate_leakage_preserve_test(
    splits: dict[str, pd.DataFrame],
) -> dict[str, pd.DataFrame]:
    """Keep the original test rows unchanged; remove duplicate texts from train/validation.

    Exact-text deduplication only. The returned frames retain the original columns and order.
    """
    train = splits["train"].copy()
    validation = splits["validation"].copy()
    test = splits["test"].copy()

    # A duplicate text inside the test set would require a separate documented decision.
    if test["text"].duplicated().any():
        raise ValueError("The supplied test split contains duplicate texts; review manually.")

    train = train.drop_duplicates(subset="text", keep="first")
    test_texts = set(test["text"])
    train = train.loc[~train["text"].isin(test_texts)].copy()

    validation = validation.drop_duplicates(subset="text", keep="first")
    already_seen = set(test["text"]) | set(train["text"])
    validation = validation.loc[~validation["text"].isin(already_seen)].copy()

    result = {
        "train": train.reset_index(drop=True),
        "validation": validation.reset_index(drop=True),
        "test": test.reset_index(drop=True),
    }
    return result
