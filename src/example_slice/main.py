"""Entrypoint for the example slice.

Wires the slice's config, data, and (placeholder) training loop together.
Copy this slice and replace the placeholder logic to start a new experiment.

Usage::

    python -m example_slice.main \
        --config src/example_slice/config.yaml
"""

import argparse
from pathlib import Path

from example_slice.scripts.data import load_samples
from shared.config import load_config

DEFAULT_CONFIG = Path(__file__).parent / "config.yaml"


def parse_args() -> argparse.Namespace:
    """Build the CLI argparser and return parsed args."""
    parser = argparse.ArgumentParser(description="Run the example slice.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    return parser.parse_args()


def run(config_path: Path) -> None:
    """Run the example slice end to end.

    Args:
        config_path: Path to the slice's YAML config.
    """
    config = load_config(config_path)
    data_cfg = config["data"]
    metadata_csv = Path(data_cfg["metadata_csv"])
    split_col = data_cfg["split_col"]

    samples = load_samples(metadata_csv, split="train", split_col=split_col)
    print(f"Loaded {len(samples)} train samples from {metadata_csv}")
    # TODO: build model, train, evaluate.


def main() -> None:
    """Parse args and run the slice."""
    args = parse_args()
    run(args.config)


if __name__ == "__main__":
    main()
