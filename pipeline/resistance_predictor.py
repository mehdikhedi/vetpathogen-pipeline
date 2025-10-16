"""Mock antimicrobial resistance predictor for the pipeline demo."""

from __future__ import annotations

import random
from typing import Iterable

import pandas as pd

RISK_LEVELS: tuple[str, ...] = ("Low", "Medium", "High")


def assign_random_risk(_: Iterable[object] | int) -> str:
    """Return a random resistance risk label."""

    return random.choice(RISK_LEVELS)


def predict_resistance(df: pd.DataFrame, *, seed: int | None = None) -> pd.DataFrame:
    """
    Append a `resistance_risk` column populated with random risk levels.

    Parameters
    ----------
    df:
        DataFrame of isolates.
    seed:
        Optional random seed for reproducibility during testing.
    """

    if seed is not None:
        random.seed(seed)

    df = df.copy()
    df["resistance_risk"] = [random.choice(RISK_LEVELS) for _ in range(len(df))]
    return df


def main() -> None:
    """CLI helper: load isolates and print assigned resistance risks."""

    import argparse

    parser = argparse.ArgumentParser(
        description="Assign mock antimicrobial resistance risk levels to isolates."
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/isolates.csv",
        help="CSV file containing isolate metadata.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducible outcomes.",
    )
    args = parser.parse_args()

    isolates = pd.read_csv(args.input)
    predictions = predict_resistance(isolates, seed=args.seed)
    print(predictions[["id", "resistance_risk"]])


if __name__ == "__main__":
    main()
