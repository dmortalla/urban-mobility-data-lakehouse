"""Temporary pipeline entry point for Milestone 1.

Later milestones will expand this into a full orchestrated pipeline:
download -> bronze -> silver -> gold -> warehouse.
"""

from __future__ import annotations

from src.logging_utils import get_logger, setup_logging

LOGGING_CONFIG_PATH = "config/logging.yaml"


def main() -> None:
    """Run the placeholder pipeline workflow."""
    setup_logging(LOGGING_CONFIG_PATH)
    logger = get_logger(__name__)

    logger.info("Urban Mobility Data Lakehouse pipeline initialized.")
    logger.info("Milestone 1 scaffold is ready.")
    logger.info("Next step: implement raw data download and Bronze ingestion.")


if __name__ == "__main__":
    main()