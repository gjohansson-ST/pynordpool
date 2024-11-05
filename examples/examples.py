import asyncio

import aiohttp
import datetime
from pynordpool import NordpoolClient, Currency


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        setup = NordpoolClient(session)
        output = await setup.async_get_delivery_period(
            datetime.datetime.now(), Currency.EUR, ["SE3"]
        )
        print(output)


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
