"""Rule-based classifier for mock pathogen species prediction."""

from __future__ import annotations

import pandas as pd


def classify_species(sequence: str) -> str:
    """Return a predicted species label based on simple pattern heuristics."""

    seq = sequence.upper()

    if "GCG" in seq:
        return "Escherichia_coli"
    if "CCC" in seq:
        return "Pseudomonas_aeruginosa"
    return "Staphylococcus_aureus"


def classify(df: pd.DataFrame) -> pd.DataFrame:
    """
    Append a `predicted_species` column using the heuristic classifier.

    Parameters
    ----------
    df:
        DataFrame with at least a `sequence` column.
    """

    if "sequence" not in df.columns:
        raise KeyError("Input dataframe must contain a 'sequence' column.")

    df = df.copy()
    df["predicted_species"] = df["sequence"].map(classify_species)
    return df


def main() -> None:
    """CLI helper: load isolates and print predicted species."""

    import argparse

    parser = argparse.ArgumentParser(description="Classify isolates by sequence patterns.")
    parser.add_argument(
        "--input",
        type=str,
        default="data/isolates.csv",
        help="CSV file containing isolate data with a sequence column.",
    )
    args = parser.parse_args()

    isolates = pd.read_csv(args.input)
    classified = classify(isolates)
    print(classified[["id", "predicted_species"]])


if __name__ == "__main__":
    main()
