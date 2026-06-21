"""Dataset / dataloader plumbing for the example slice."""

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from shared.data_utils import split_frame


@dataclass
class Sample:
    """One example sample loaded from the metadata table."""

    sample_id: str
    path: Path
    label: str


def load_samples(
    metadata_csv: Path,
    split: str,
    split_col: str = "split",
) -> list[Sample]:
    """Load samples for a given split from the metadata CSV.

    Args:
        metadata_csv: Path to the metadata table.
        split: Which split to load (e.g. "train" or "test").
        split_col: Name of the split column in the table.

    Returns:
        The samples belonging to ``split``.

    Raises:
        KeyError: If ``split`` is not present in the table.
    """
    frame: pd.DataFrame = pd.read_csv(metadata_csv)
    splits = split_frame(frame, split_col=split_col)
    if split not in splits:
        raise KeyError(f"Split {split!r} not found in {metadata_csv}")
    records = splits[split].to_dict(orient="records")
    return [
        Sample(
            sample_id=str(record["sample_id"]),
            path=Path(str(record["path"])),
            label=str(record["label"]),
        )
        for record in records
    ]
