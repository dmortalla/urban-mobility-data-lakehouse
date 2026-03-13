"""Path utilities for the Urban Mobility Data Lakehouse project."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def ensure_directories(paths: Iterable[str | Path]) -> None:
    """Create directories if they do not already exist.

    Args:
        paths: Iterable of directory paths.
    """
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)


def project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parents[2]