"""Exceptions for Nord Pool."""

from typing import Any


class NordPoolError(Exception):
    """Error from Nord Pool api."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)
