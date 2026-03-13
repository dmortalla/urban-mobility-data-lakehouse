"""
Bronze ingestion workflow for NYC taxi trip data.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.bronze.write_bronze_table import write_bronze_parquet
from src.transform.add_metadata import add_ingestion_metadata
from src.validate.schema_validator import validate_required_columns


def ingest_raw_parquet_to_bronze(
    raw_file_path: str | Path,
    bronze_output_dir: str | Path,
) -> Path:
    """
    Read a raw parquet file, validate it, add ingestion metadata,
    and write it to the Bronze layer.

    Args:
        raw_file_path: Path to the raw parquet file.
        bronze_output_dir: Directory for Bronze output.

    Returns:
        Path to the written Bronze parquet file.
    """
    raw_file_path = Path(raw_file_path)

    df = pd.read_parquet(raw_file_path)
    validate_required_columns(df)

    enriched_df = add_ingestion_metadata(
        df=df,
        source_file=raw_file_path.name,
    )

    output_filename = f"bronze_{raw_file_path.name}"
    return write_bronze_parquet(
        df=enriched_df,
        output_dir=bronze_output_dir,
        output_filename=output_filename,
    )