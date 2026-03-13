"""
Write Silver layer parquet files for the Urban Mobility Data Lakehouse.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.transform.bronze_to_silver_cleaning import clean_bronze_dataframe


def write_silver_table(
    bronze_file_path: Path,
    silver_output_dir: Path,
) -> Path:
    """
    Transform a Bronze parquet file into a cleaned Silver parquet file.

    Args:
        bronze_file_path: Path to the Bronze parquet file.
        silver_output_dir: Directory where the Silver file should be written.

    Returns:
        Path to the created Silver parquet file.
    """

    df = pd.read_parquet(bronze_file_path)

    cleaned_df = clean_bronze_dataframe(df)

    silver_filename = f"silver_{bronze_file_path.name}"
    silver_path = silver_output_dir / silver_filename

    cleaned_df.to_parquet(silver_path, index=False)

    return silver_path