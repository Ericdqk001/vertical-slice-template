"""Tests for example_slice.scripts.data."""

from pathlib import Path

import pytest

from example_slice.scripts.data import load_samples


def test_load_samples_returns_only_requested_split(metadata_csv: Path) -> None:
    train = load_samples(metadata_csv, split="train")
    assert len(train) == 2
    assert {s.sample_id for s in train} == {"s1", "s2"}


def test_load_samples_unknown_split_raises(metadata_csv: Path) -> None:
    with pytest.raises(KeyError):
        load_samples(metadata_csv, split="val")
