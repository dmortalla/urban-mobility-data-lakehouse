"""
Schema validation utilities for taxi datasets.
"""

from typing import List
import pandas as pd


REQUIRED_COLUMNS: List[str] = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime",
    "passenger_count",
    "trip_distance",
]


def validate_required_columns(df: pd.DataFrame) -> None:
    """
    Ensure required columns exist in the dataframe.

    Raises
    ------
    ValueError
        If required columns are missing.
    """

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing:
        raise ValueError(
            f"Dataset missing required columns: {missing}"
        )