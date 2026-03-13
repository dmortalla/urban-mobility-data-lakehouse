"""
Tests for Silver-to-Gold aggregation logic.
"""

from __future__ import annotations

import pandas as pd

from src.transform.silver_to_gold_aggregations import (
    build_daily_trip_summary,
    build_hourly_demand_summary,
    build_payment_type_revenue,
)


def make_sample_silver_df() -> pd.DataFrame:
    """
    Create a small sample Silver dataframe for testing.
    """
    return pd.DataFrame(
        {
            "pickup_date": ["2024-01-01", "2024-01-01", "2024-01-02"],
            "pickup_hour": [8, 9, 8],
            "trip_distance": [2.0, 3.0, 4.0],
            "fare_amount": [10.0, 15.0, 20.0],
            "total_amount": [12.0, 18.0, 25.0],
            "payment_type": [1, 2, 1],
        }
    )


def test_build_daily_trip_summary_returns_expected_columns() -> None:
    """
    Ensure the daily trip summary has the expected columns.
    """
    df = make_sample_silver_df()
    result = build_daily_trip_summary(df)

    assert "pickup_date" in result.columns
    assert "trip_count" in result.columns
    assert "avg_trip_distance" in result.columns
    assert "avg_fare" in result.columns
    assert "total_revenue" in result.columns


def test_build_hourly_demand_summary_returns_expected_columns() -> None:
    """
    Ensure the hourly demand summary has the expected columns.
    """
    df = make_sample_silver_df()
    result = build_hourly_demand_summary(df)

    assert "pickup_hour" in result.columns
    assert "trip_count" in result.columns
    assert "avg_trip_distance" in result.columns
    assert "avg_fare" in result.columns


def test_build_payment_type_revenue_returns_expected_columns() -> None:
    """
    Ensure the payment revenue summary has the expected columns.
    """
    df = make_sample_silver_df()
    result = build_payment_type_revenue(df)

    assert "payment_type" in result.columns
    assert "trip_count" in result.columns
    assert "total_revenue" in result.columns