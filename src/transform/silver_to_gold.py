"""
Gold transformation orchestration logic.
"""

from __future__ import annotations

from pathlib import Path

from src.gold.write_gold_tables import write_gold_tables


def transform_silver_to_gold(
    silver_file_path: str | Path,
    gold_output_dir: str | Path,
) -> dict[str, Path]:
    """
    Transform a Silver parquet file into Gold summary tables.

    Args:
        silver_file_path: Path to the Silver parquet file.
        gold_output_dir: Directory where Gold tables should be written.

    Returns:
        Dictionary of written Gold table paths.
    """
    silver_file_path = Path(silver_file_path)
    gold_output_dir = Path(gold_output_dir)

    return write_gold_tables(
        silver_file_path=silver_file_path,
        gold_output_dir=gold_output_dir,
    )