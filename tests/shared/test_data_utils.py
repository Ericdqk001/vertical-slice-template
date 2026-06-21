"""Tests for shared.data_utils."""

import pandas as pd
import pytest

from shared.data_utils import split_frame


def test_split_frame_partitions_by_label() -> None:
    frame = pd.DataFrame(
        {
            "sample_id": ["a", "b", "c"],
            "split": ["train", "test", "train"],
        }
    )
    splits = split_frame(frame)
    assert set(splits) == {"train", "test"}
    assert len(splits["train"]) == 2
    assert len(splits["test"]) == 1


def test_split_frame_missing_column_raises() -> None:
    frame = pd.DataFrame({"sample_id": ["a"]})
    with pytest.raises(KeyError):
        split_frame(frame)
