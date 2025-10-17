"""Orchestrate the VetPathogen pipeline to generate a consolidated report."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from pipeline.classify_pathogen import classify
from pipeline.resistance_predictor import predict_resistance


def generate_report(
    input_csv: str | Path = Path("data/isolates.csv"),
    output_csv: str | Path = Path("data/report.csv"),
    *,
    seed: int | None = None,
) -> pd.DataFrame:
    """
    Run the pipeline and persist the final dataframe.

    Parameters
    ----------
    input_csv:
        Path to the isolates dataset.
    output_csv:
        Destination for the generated report.
    seed:
        Optional seed to make the resistance prediction deterministic.
    """

    input_path = Path(input_csv)
    if not input_path.exists():
        raise FileNotFoundError(f"Isolate dataset not found: {input_path}")

    isolates = pd.read_csv(input_path)
    classified = classify(isolates)
    enriched = predict_resistance(classified, seed=seed)

    output_path = Path(output_csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    enriched.to_csv(output_path, index=False)
    return enriched


def main() -> None:
    """CLI entry point for generating the pipeline report."""

    import argparse

    parser = argparse.ArgumentParser(
        description="Generate the VetPathogen pipeline report from isolate data."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/isolates.csv"),
        help="Path to the isolates CSV dataset.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/report.csv"),
        help="Destination CSV for the consolidated report.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducible resistance predictions.",
    )
    args = parser.parse_args()

    report_df = generate_report(args.input, args.output, seed=args.seed)
    print(report_df)
    print(f"\nReport saved to {Path(args.output).resolve()}")


if __name__ == "__main__":
    main()
