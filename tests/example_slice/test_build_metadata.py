"""Tests for example_slice.build_metadata."""

from pathlib import Path

import pytest

from example_slice import build_metadata as bm


@pytest.fixture
def raw_data_dir(tmp_path: Path) -> Path:
    """Create three empty raw sample files."""
    for name in ("s1", "s2", "s3"):
        (tmp_path / f"{name}.png").write_bytes(b"")
    return tmp_path


def test_build_metadata_joins_labels(raw_data_dir: Path) -> None:
    labels = {"s1": "A", "s2": "B"}
    frame = bm.build_metadata(raw_data_dir, labels)
    assert list(frame.columns) == ["sample_id", "path", "label", "split"]
    assert len(frame) == 3
    by_id = dict(zip(frame.sample_id, frame.label, strict=True))
    assert by_id["s1"] == "A"
    assert by_id["s3"] == "unknown"


def test_load_labels_monkeypatched(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(bm, "_load_labels", lambda: {"s1": "A"})
    assert bm._load_labels() == {"s1": "A"}
