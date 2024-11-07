"""Utils for Nord Pool."""

from __future__ import annotations

import datetime as dt


async def parse_datetime(dt_str: str) -> dt.datetime:
    """Parse a string and return a datetime.datetime.

    input: 2024-11-04T23:00:00Z or 2024-11-04T12:15:03.8832404Z
    """
    return dt.datetime.fromisoformat(dt_str)
