"""Tests for configuration loading and validation."""

from __future__ import annotations

from src.config import load_yaml_config, validate_pipeline_config


def test_load_pipeline_config_returns_dict() -> None:
    """Ensure the pipeline config loads as a dictionary."""
    config = load_yaml_config("config/pipeline.yaml")
    assert isinstance(config, dict)


def test_validate_pipeline_config_passes_for_valid_config() -> None:
    """Ensure a valid pipeline config passes validation."""
    config = load_yaml_config("config/pipeline.yaml")
    validate_pipeline_config(config)