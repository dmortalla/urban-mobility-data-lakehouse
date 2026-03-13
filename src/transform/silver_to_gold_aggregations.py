"""
Gold aggregation logic for the Urban Mobility Data Lakehouse.
"""

from __future__ import annotations

import pandas as pd


def build_daily_trip_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build daily trip summary from Silver data.

    Returns aggregated metrics per day.
    """

    summary = (
        df.groupby("pickup_date")
        .agg(
            trip_count=("trip_distance", "count"),
            avg_trip_distance=("trip_distance", "mean"),
            avg_fare=("fare_amount", "mean"),
            total_revenue=("total_amount", "sum"),
        )
        .reset_index()
    )

    return summary


def build_hourly_demand_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build hourly demand summary.
    """

    hourly = (
        df.groupby("pickup_hour")
        .agg(
            trip_count=("trip_distance", "count"),
            avg_trip_distance=("trip_distance", "mean"),
            avg_fare=("fare_amount", "mean"),
        )
        .reset_index()
    )

    return hourly


def build_payment_type_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Revenue breakdown by payment type.
    """

    payment = (
        df.groupby("payment_type")
        .agg(
            trip_count=("trip_distance", "count"),
            total_revenue=("total_amount", "sum"),
        )
        .reset_index()
    )

    return payment