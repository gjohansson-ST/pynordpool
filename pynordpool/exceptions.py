"""Exceptions for Sensibo."""

from typing import Any


class NordpoolError(Exception):
    """Error from Nordpool api."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)
