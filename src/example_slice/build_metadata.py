"""Build the example slice's metadata table from raw inputs.

Joins biological / experimental labels onto the per-sample rows at build
time and writes a single CSV with a ``split`` column embedded, so every
downstream consumer reads one self-describing table.

Usage::

    python -m example_slice.build_metadata \
        --data-dir data/raw \
        --output data/example_metadata.csv
"""

import argparse
from pathlib import Path

import pandas as pd


def _load_labels() -> dict[str, str]:
    """Return the sample-id -> label mapping.

    Replace this stub with a real load (e.g. from a committed JSON/CSV).
    Tests monkeypatch this function to decouple from real label files.
    """
    return {}


def build_metadata(data_dir: Path, labels: dict[str, str]) -> pd.DataFrame:
    """Scan ``data_dir`` for samples and join labels into one table.

    Args:
        data_dir: Directory containing the raw per-sample files.
        labels: Mapping from sample id to its biological label.

    Returns:
        A metadata frame with columns: sample_id, path, label, split.
    """
    rows: list[dict[str, str]] = []
    for path in sorted(data_dir.glob("*")):
        if not path.is_file():
            continue
        sample_id = path.stem
        rows.append(
            {
                "sample_id": sample_id,
                "path": str(path),
                "label": labels.get(sample_id, "unknown"),
                "split": "train",
            }
        )
    return pd.DataFrame(rows)


def parse_args() -> argparse.Namespace:
    """Build the CLI argparser and return parsed args."""
    parser = argparse.ArgumentParser(description="Build example slice metadata.")
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    """Build the metadata table and write it to the output CSV."""
    args = parse_args()
    frame = build_metadata(args.data_dir, _load_labels())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output, index=False)
    print(f"Wrote {len(frame)} rows to {args.output}")


if __name__ == "__main__":
    main()
