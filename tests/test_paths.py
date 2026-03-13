"""Tests for path utilities."""

from __future__ import annotations

from pathlib import Path

from src.utils.paths import project_root


def test_project_root_exists() -> None:
    """Ensure the project root path exists."""
    root = project_root()
    assert isinstance(root, Path)
    assert root.exists()