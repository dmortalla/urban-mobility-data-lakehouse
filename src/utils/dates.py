"""Date utilities for the Urban Mobility Data Lakehouse project."""

from __future__ import annotations


def month_to_string(month: int) -> str:
    """Convert integer month to zero-padded string.

    Args:
        month: Month integer.

    Returns:
        Zero-padded month string.

    Raises:
        ValueError: If month is outside 1..12.
    """
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    return f"{month:02d}"