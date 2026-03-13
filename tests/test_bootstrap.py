"""Tests for project bootstrap behavior."""

from __future__ import annotations

from src.validate.bronze_checks import validate_raw_file_exists


def test_validate_raw_file_exists_for_missing_file() -> None:
    """Ensure missing files correctly return False."""
    assert validate_raw_file_exists("data/raw/does_not_exist.parquet") is False