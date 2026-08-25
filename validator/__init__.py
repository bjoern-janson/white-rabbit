"""Deterministic provenance validation for White Rabbit research state."""

from importlib import import_module


__all__ = ["OUTCOMES", "ValidationReport", "validate_file", "validate_state"]


def __getattr__(name):
    if name not in __all__:
        raise AttributeError(name)
    return getattr(import_module(".validate", __name__), name)
