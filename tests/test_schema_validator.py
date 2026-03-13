"""
Tests for schema validation utilities.
"""

from __future__ import annotations

import pandas as pd
import pytest

from src.validate.schema_validator import validate_required_columns


def test_validate_required_columns_passes_for_valid_dataframe() -> None:
    """
    Ensure validation passes when all required columns are present.
    """
    df = pd.DataFrame(
        {
            "tpep_pickup_datetime": ["2024-01-01 10:00:00"],
            "tpep_dropoff_datetime": ["2024-01-01 10:15:00"],
            "passenger_count": [1],
            "trip_distance": [2.5],
        }
    )

    validate_required_columns(df)


def test_validate_required_columns_raises_for_missing_columns() -> None:
    """
    Ensure validation fails when required columns are missing.
    """
    df = pd.DataFrame(
        {
            "tpep_pickup_datetime": ["2024-01-01 10:00:00"],
            "passenger_count": [1],
        }
    )

    with pytest.raises(ValueError):
        validate_required_columns(df)