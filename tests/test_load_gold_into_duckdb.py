"""
Tests for loading Gold parquet files into DuckDB.
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path
import duckdb

from src.warehouse.load_gold_into_duckdb import load_gold_tables_into_duckdb


def test_load_gold_tables_into_duckdb(tmp_path: Path) -> None:
    """
    Ensure Gold parquet files are correctly loaded into DuckDB.
    """

    gold_dir = tmp_path / "gold"
    gold_dir.mkdir()

    df = pd.DataFrame(
        {
            "pickup_date": ["2024-01-01"],
            "trip_count": [10],
        }
    )

    parquet_file = gold_dir / "daily_trip_summary_test.parquet"
    df.to_parquet(parquet_file, index=False)

    db_path = tmp_path / "analytics.duckdb"

    load_gold_tables_into_duckdb(gold_dir, db_path)

    with duckdb.connect(str(db_path)) as con:
        row = con.execute("SELECT COUNT(*) FROM daily_trip_summary_test").fetchone()

    assert row is not None
    assert row[0] == 1