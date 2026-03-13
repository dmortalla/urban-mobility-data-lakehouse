"""Bootstrap required folders and validate core project configuration."""

from __future__ import annotations

from src.config import load_yaml_config, validate_pipeline_config
from src.exceptions import BootstrapError
from src.logging_utils import get_logger, setup_logging
from src.utils.paths import ensure_directories

PIPELINE_CONFIG_PATH = "config/pipeline.yaml"
LOGGING_CONFIG_PATH = "config/logging.yaml"


def main() -> None:
    """Create required directories and validate base configuration."""
    setup_logging(LOGGING_CONFIG_PATH)
    logger = get_logger(__name__)

    try:
        config = load_yaml_config(PIPELINE_CONFIG_PATH)
        validate_pipeline_config(config)

        path_config = config["paths"]
        required_directories = [
            "data/raw",
            "data/sample",
            "data/lake",
            "data/lake/bronze",
            "data/lake/silver",
            "data/lake/gold",
            path_config["logs"],
            path_config["warehouse"],
            "docs/screenshots",
        ]

        ensure_directories(required_directories)
        logger.info("Project bootstrap completed successfully.")

    except Exception as exc:
        raise BootstrapError(f"Project bootstrap failed: {exc}") from exc


if __name__ == "__main__":
    main()