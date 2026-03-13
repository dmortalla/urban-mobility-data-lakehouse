"""
Write Gold layer parquet tables for the Urban Mobility Data Lakehouse.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.transform.silver_to_gold_aggregations import (
    build_daily_trip_summary,
    build_hourly_demand_summary,
    build_payment_type_revenue,
)


def write_gold_tables(
    silver_file_path: Path,
    gold_output_dir: Path,
) -> dict[str, Path]:
    """
    Read a Silver parquet file, build Gold summary tables,
    and write them as parquet files.

    Args:
        silver_file_path: Path to the Silver parquet file.
        gold_output_dir: Directory where Gold tables should be written.

    Returns:
        Dictionary mapping Gold table names to output paths.
    """
    gold_output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_parquet(silver_file_path)

    daily_summary = build_daily_trip_summary(df)
    hourly_summary = build_hourly_demand_summary(df)
    payment_summary = build_payment_type_revenue(df)

    silver_stem = silver_file_path.stem

    output_paths = {
        "daily_trip_summary": gold_output_dir / f"daily_trip_summary_{silver_stem}.parquet",
        "hourly_demand_summary": gold_output_dir / f"hourly_demand_summary_{silver_stem}.parquet",
        "payment_type_revenue": gold_output_dir / f"payment_type_revenue_{silver_stem}.parquet",
    }

    daily_summary.to_parquet(output_paths["daily_trip_summary"], index=False)
    hourly_summary.to_parquet(output_paths["hourly_demand_summary"], index=False)
    payment_summary.to_parquet(output_paths["payment_type_revenue"], index=False)

    return output_paths