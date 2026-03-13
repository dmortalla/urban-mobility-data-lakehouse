"""
Cleaning and feature engineering for Bronze → Silver transformation.
"""

from __future__ import annotations

import pandas as pd


def clean_bronze_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and enrich a Bronze dataframe for the Silver layer.

    Adds derived columns and removes clearly invalid records.

    Args:
        df: Bronze dataframe.

    Returns:
        Cleaned dataframe ready for Silver.
    """

    cleaned = df.copy()

    # Convert timestamps
    cleaned["tpep_pickup_datetime"] = pd.to_datetime(cleaned["tpep_pickup_datetime"])
    cleaned["tpep_dropoff_datetime"] = pd.to_datetime(cleaned["tpep_dropoff_datetime"])

    # Trip duration
    cleaned["trip_duration_minutes"] = (
        cleaned["tpep_dropoff_datetime"] - cleaned["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    # Derived time features
    cleaned["pickup_date"] = cleaned["tpep_pickup_datetime"].dt.date
    cleaned["pickup_hour"] = cleaned["tpep_pickup_datetime"].dt.hour

    # Basic validity checks
    cleaned = cleaned[cleaned["trip_distance"] > 0]
    cleaned = cleaned[cleaned["trip_duration_minutes"] > 0]

    # Fare per mile if fare_amount exists
    if "fare_amount" in cleaned.columns:
        cleaned["fare_per_mile"] = cleaned["fare_amount"] / cleaned["trip_distance"]

    return cleaned