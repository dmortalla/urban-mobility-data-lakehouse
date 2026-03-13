"""Logging helpers for the Urban Mobility Data Lakehouse project."""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path

import yaml


def setup_logging(logging_config_path: str | Path) -> None:
    """Set up project logging from a YAML configuration file.

    Args:
        logging_config_path: Path to the logging config YAML file.
    """
    logging_config_path = Path(logging_config_path)

    with logging_config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    log_file = Path("logs/project.log")
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.config.dictConfig(config)


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger.

    Args:
        name: Logger name.

    Returns:
        Configured logger instance.
    """
    return logging.getLogger(name)