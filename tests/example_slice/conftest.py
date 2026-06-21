"""Shared fixtures for example_slice tests."""

from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture
def metadata_csv(tmp_path: Path) -> Path:
    """Write a tiny synthetic metadata CSV and return its path.

    Two train rows and one test row, mirroring the schema produced by
    ``example_slice.build_metadata``.
    """
    frame = pd.DataFrame(
        {
            "sample_id": ["s1", "s2", "s3"],
            "path": ["data/s1.png", "data/s2.png", "data/s3.png"],
            "label": ["A", "B", "A"],
            "split": ["train", "train", "test"],
        }
    )
    out = tmp_path / "metadata.csv"
    frame.to_csv(out, index=False)
    return out
