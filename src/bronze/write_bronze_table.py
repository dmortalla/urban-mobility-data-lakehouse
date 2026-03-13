"""
Bronze layer write utilities.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_bronze_parquet(
    df: pd.DataFrame,
    output_dir: str | Path,
    output_filename: str,
) -> Path:
    """
    Write a dataframe to the Bronze layer as a parquet file.

    Args:
        df: Dataframe to write.
        output_dir: Bronze output directory.
        output_filename: Name of the parquet output file.

    Returns:
        Path to the written parquet file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / output_filename
    df.to_parquet(output_path, index=False)

    return output_path