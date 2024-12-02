"""Exceptions for Nord Pool."""

from aiohttp import ClientError, ClientResponseError


class NordPoolError(ClientError):
    """Base error from Nord Pool api."""


class NordPoolConnectionError(NordPoolError):
    """Connection error from Nord Pool api."""


class NordPoolResponseError(ClientResponseError):
    """Response error from Nord Pool api.

    aiohttp raises ClientResponseError.
    """


class NordPoolEmptyResponseError(NordPoolError):
    """Empty response error from Nord Pool api.

    Response.status = 204
    """


class NordPoolAuthenticationError(NordPoolError):
    """Response error from Nord Pool api.

    Response.status = 401 or 403
    """
