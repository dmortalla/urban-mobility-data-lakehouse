"""
Download utilities for NYC taxi trip data.
"""

from __future__ import annotations

from pathlib import Path

import requests

from src.utils.dates import month_to_string


def build_taxi_data_url(
    taxi_type: str,
    year: int,
    month: int,
    base_url: str,
) -> str:
    """
    Build the NYC taxi parquet download URL.

    Args:
        taxi_type: Taxi dataset type, such as 'yellow'.
        year: Four-digit year.
        month: Month number.
        base_url: Base dataset URL.

    Returns:
        Full download URL for the parquet file.
    """
    month_str = month_to_string(month)
    filename = f"{taxi_type}_tripdata_{year}-{month_str}.parquet"
    return f"{base_url}/{filename}"


def build_taxi_output_path(
    raw_data_dir: str | Path,
    taxi_type: str,
    year: int,
    month: int,
) -> Path:
    """
    Build the local output path for a raw taxi parquet file.

    Args:
        raw_data_dir: Directory where raw files are stored.
        taxi_type: Taxi dataset type.
        year: Four-digit year.
        month: Month number.

    Returns:
        Full local output path.
    """
    raw_data_dir = Path(raw_data_dir)
    month_str = month_to_string(month)
    filename = f"{taxi_type}_tripdata_{year}-{month_str}.parquet"
    return raw_data_dir / filename


def download_file(url: str, output_path: str | Path) -> Path:
    """
    Download a file from a URL to disk.

    Args:
        url: Source URL.
        output_path: Destination path.

    Returns:
        Path to the downloaded file.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(url, timeout=120)
    response.raise_for_status()

    output_path.write_bytes(response.content)
    return output_path