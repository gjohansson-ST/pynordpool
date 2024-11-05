"""Utils for Nordpool."""

from __future__ import annotations

import datetime as dt

from aiozoneinfo import async_get_time_zone

CET = "Europe/Stockholm"


async def parse_utc_datetime(dt_str: str) -> dt.datetime:
    """Parse a string and return a datetime.datetime.

    input: 2024-11-04T23:00:00Z
    """

    result = dt.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ")
    return result.replace(tzinfo=dt.timezone.utc)


async def parse_cet_datetime(dt_str: str) -> dt.datetime:
    """Parse a string and return a datetime.datetime.

    input: 2024-11-04T12:15:03.8832404Z
    """

    result = dt.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%f4Z")
    tz = await async_get_time_zone(CET)
    return result.replace(tzinfo=tz)
