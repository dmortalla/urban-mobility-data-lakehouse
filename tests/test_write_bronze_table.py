"""
Tests for Bronze parquet writing.
"""

from __future__ import annotations

import pandas as pd

from src.bronze.write_bronze_table import write_bronze_parquet


def test_write_bronze_parquet_creates_output_file(tmp_path) -> None:
    """
    Ensure the Bronze writer creates a parquet file.
    """
    df = pd.DataFrame({"trip_distance": [1.0, 2.0]})

    output_path = write_bronze_parquet(
        df=df,
        output_dir=tmp_path,
        output_filename="bronze_test.parquet",
    )

    assert output_path.exists()
    assert output_path.name == "bronze_test.parquet"