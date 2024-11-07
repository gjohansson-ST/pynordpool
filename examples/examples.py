"""Example usage of the library."""

import asyncio
import datetime

import aiohttp

from pynordpool import NordPoolClient
from pynordpool.const import Currency


async def main(loop: asyncio.AbstractEventLoop) -> None:
    """Print the delivery period."""
    async with aiohttp.ClientSession(loop=loop) as session:
        client = NordPoolClient(session)
        output = await client.async_get_delivery_period(
            datetime.datetime.now(), Currency.EUR, ["SE3"]
        )
        print(output)  # noqa: T201


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
