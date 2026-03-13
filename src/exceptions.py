"""Custom exceptions for the Urban Mobility Data Lakehouse project."""


class ConfigurationError(Exception):
    """Raised when required configuration is missing or invalid."""


class DataValidationError(Exception):
    """Raised when data fails one or more validation checks."""


class BootstrapError(Exception):
    """Raised when project bootstrapping fails."""