"""
Load Gold parquet tables into DuckDB for analytics queries.
"""

from __future__ import annotations

from pathlib import Path
import duckdb


def load_gold_tables_into_duckdb(
    gold_dir: str | Path,
    db_path: str | Path,
) -> None:
    """
    Load Gold parquet files into DuckDB tables.

    Args:
        gold_dir: Directory containing Gold parquet files
        db_path: Path to DuckDB database file
    """

    gold_dir = Path(gold_dir)
    db_path = Path(db_path)

    con = duckdb.connect(str(db_path))

    parquet_files = sorted(gold_dir.glob("*.parquet"))

    if not parquet_files:
        raise ValueError("No Gold parquet files found.")

    for parquet_file in parquet_files:
        table_name = parquet_file.stem.replace("-", "_").replace(".", "_")

        con.execute(
            f"""
            CREATE OR REPLACE TABLE {table_name}
            AS SELECT * FROM read_parquet('{parquet_file}')
            """
        )

    con.close()