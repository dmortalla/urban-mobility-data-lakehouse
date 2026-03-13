"""Validation checks for Bronze layer data."""

from __future__ import annotations

from pathlib import Path


def validate_raw_file_exists(file_path: str | Path) -> bool:
    """Check whether a raw file exists.

    Args:
        file_path: Path to a raw file.

    Returns:
        True if the file exists, otherwise False.
    """
    return Path(file_path).exists()