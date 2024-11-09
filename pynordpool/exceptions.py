"""Exceptions for Nord Pool."""

from typing import Any


class NordPoolError(Exception):
    """Error from Nord Pool api."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)


class NordPoolConnectionError(NordPoolError):
    """Connection error from Nord Pool api."""


class NordPoolResponseError(NordPoolError):
    """Response error from Nord Pool api."""


class NordPoolEmptyResponseError(NordPoolError):
    """Empty response error from Nord Pool api."""


class NordPoolAuthenticationError(NordPoolError):
    """Response error from Nord Pool api."""
