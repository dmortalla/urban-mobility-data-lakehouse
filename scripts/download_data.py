"""Download raw NYC taxi parquet files for the Urban Mobility Data Lakehouse."""

from __future__ import annotations

from pathlib import Path

import requests

from src.config import load_yaml_config, validate_pipeline_config
from src.logging_utils import get_logger, setup_logging
from src.utils.dates import month_to_string
from src.utils.paths import ensure_directories

PIPELINE_CONFIG_PATH = "config/pipeline.yaml"
LOGGING_CONFIG_PATH = "config/logging.yaml"


def download_file(url: str, output_path: Path) -> None:
    """Download a file from a URL to disk.

    Args:
        url: Source URL.
        output_path: Destination file path.
    """
    response = requests.get(url, timeout=120)
    response.raise_for_status()

    output_path.write_bytes(response.content)


def main() -> None:
    """Download configured taxi parquet files to the raw data directory."""
    setup_logging(LOGGING_CONFIG_PATH)
    logger = get_logger(__name__)

    config = load_yaml_config(PIPELINE_CONFIG_PATH)
    validate_pipeline_config(config)

    raw_data_dir = Path(config["paths"]["raw_data"])
    dataset_config = config["dataset"]

    ensure_directories([raw_data_dir])

    taxi_type = dataset_config["taxi_type"]
    year = dataset_config["year"]
    months = dataset_config["months"]

    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"

    for month in months:
        month_str = month_to_string(month)
        filename = f"{taxi_type}_tripdata_{year}-{month_str}.parquet"
        file_url = f"{base_url}/{filename}"
        output_path = raw_data_dir / filename

        if output_path.exists():
            logger.info("File already exists, skipping: %s", output_path)
            continue

        logger.info("Downloading %s", file_url)
        download_file(file_url, output_path)
        logger.info("Saved to %s", output_path)


if __name__ == "__main__":
    main()