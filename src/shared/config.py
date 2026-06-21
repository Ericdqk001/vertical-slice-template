"""Config loading helpers shared across slices."""

from pathlib import Path
from typing import Any

import yaml


def load_config(path: Path) -> dict[str, Any]:
    """Load a YAML config file into a dictionary.

    Args:
        path: Path to the YAML config file.

    Returns:
        The parsed config as a nested dictionary.

    Raises:
        FileNotFoundError: If ``path`` does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with path.open("r") as handle:
        return yaml.safe_load(handle)
