"""Generic data helpers shared across slices."""

import pandas as pd


def split_frame(
    frame: pd.DataFrame,
    split_col: str = "split",
) -> dict[str, pd.DataFrame]:
    """Partition a metadata frame by the value of its split column.

    Embedding all splits in one table with a ``split`` column (rather than
    keeping separate files) keeps the data join logic in one place.

    Args:
        frame: Metadata table containing a split column.
        split_col: Name of the column holding split labels (e.g. train/test).

    Returns:
        Mapping from each split label to its sub-frame.

    Raises:
        KeyError: If ``split_col`` is not a column of ``frame``.
    """
    if split_col not in frame.columns:
        raise KeyError(f"Missing split column: {split_col!r}")
    return {
        str(label): sub.reset_index(drop=True)
        for label, sub in frame.groupby(split_col)
    }
