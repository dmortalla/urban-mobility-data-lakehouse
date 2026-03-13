"""Configuration loading utilities for the Urban Mobility Data Lakehouse project."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml

from src.exceptions import ConfigurationError


def load_yaml_config(config_path: str | Path) -> Dict[str, Any]:
    """Load a YAML configuration file.

    Args:
        config_path: Path to the YAML file.

    Returns:
        Parsed configuration as a dictionary.

    Raises:
        ConfigurationError: If the file does not exist or is invalid.
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise ConfigurationError(f"Config file not found: {config_path}")

    try:
        with config_path.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        raise ConfigurationError(
            f"Unable to parse YAML config: {config_path}"
        ) from exc

    if not isinstance(config, dict):
        raise ConfigurationError(
            f"Config file must parse to a dictionary: {config_path}"
        )

    return config


def validate_pipeline_config(config: Dict[str, Any]) -> None:
    """Validate the minimum required pipeline configuration.

    Args:
        config: Parsed pipeline configuration dictionary.

    Raises:
        ConfigurationError: If required top-level keys are missing.
    """
    required_top_level_keys = ["project", "paths", "dataset", "validation", "runtime"]

    missing_keys = [key for key in required_top_level_keys if key not in config]
    if missing_keys:
        raise ConfigurationError(
            f"Missing required pipeline config keys: {missing_keys}"
        )

    required_path_keys = [
        "raw_data",
        "bronze_data",
        "silver_data",
        "gold_data",
        "logs",
        "warehouse",
    ]
    path_config = config.get("paths", {})
    missing_path_keys = [key for key in required_path_keys if key not in path_config]

    if missing_path_keys:
        raise ConfigurationError(
            f"Missing required path config keys: {missing_path_keys}"
        )