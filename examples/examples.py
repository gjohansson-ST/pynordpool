"""Example usage of the library."""

import asyncio
from datetime import datetime, timedelta

import aiohttp

from pynordpool import Currency, NordPoolClient


async def main(loop: asyncio.AbstractEventLoop) -> None:
    """Print the delivery period."""
    async with aiohttp.ClientSession(loop=loop) as session:
        client = NordPoolClient(session)
        output = await client.async_get_delivery_period(
            datetime.now(), Currency.EUR, ["SE3"]
        )
        output2 = await client.async_get_delivery_periods(
            [datetime.now(), datetime.now() + timedelta(days=1)], Currency.EUR, ["SE3"]
        )
        print(output)  # noqa: T201
        print(output2)  # noqa: T201


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
