"""
Pipeline entry point for the Urban Mobility Data Lakehouse.
"""

from __future__ import annotations

from pathlib import Path

from src.config import load_yaml_config, validate_pipeline_config
from src.extract.ingest_taxi_data import ingest_raw_parquet_to_bronze
from src.logging_utils import get_logger, setup_logging
from src.silver.write_silver_table import write_silver_table

PIPELINE_CONFIG_PATH = "config/pipeline.yaml"
LOGGING_CONFIG_PATH = "config/logging.yaml"


def main() -> None:
    """
    Run the Raw → Bronze → Silver pipeline.
    """
    setup_logging(LOGGING_CONFIG_PATH)
    logger = get_logger(__name__)

    config = load_yaml_config(PIPELINE_CONFIG_PATH)
    validate_pipeline_config(config)

    raw_data_dir = Path(config["paths"]["raw_data"])
    bronze_data_dir = Path(config["paths"]["bronze_data"])
    silver_data_dir = Path(config["paths"]["silver_data"])

    logger.info("Urban Mobility Data Lakehouse pipeline initialized.")

    # ---------- Bronze Stage ----------

    logger.info("Starting Bronze ingestion pipeline.")

    raw_files = sorted(raw_data_dir.glob("*.parquet"))

    if not raw_files:
        logger.info("No raw parquet files found in %s", raw_data_dir)
        logger.info("Run `python -m scripts.download_data` first.")
        return

    bronze_files = []

    for raw_file in raw_files:
        bronze_path = ingest_raw_parquet_to_bronze(
            raw_file_path=raw_file,
            bronze_output_dir=bronze_data_dir,
        )

        bronze_files.append(bronze_path)

        logger.info("Bronze file written to %s", bronze_path)

    logger.info("Bronze ingestion pipeline completed successfully.")

    # ---------- Silver Stage ----------

    logger.info("Starting Silver transformation pipeline.")

    for bronze_file in bronze_files:
        silver_path = write_silver_table(
            bronze_file_path=bronze_file,
            silver_output_dir=silver_data_dir,
        )

        logger.info("Silver file written to %s", silver_path)

    logger.info("Silver pipeline completed successfully.")


if __name__ == "__main__":
    main()