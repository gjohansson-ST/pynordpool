# pynordpool
python module for communicating with [Nord Pool](https://data.nordpoolgroup.com/auction/day-ahead/prices)

## Code example

### Retrieve delivery period prices

Hourly rates from provided date

```python
from pynordpool import NordPoolClient, Currency

async with aiohttp.ClientSession(loop=loop) as session:
    client = NordPoolClient(session)
    output = await client.async_get_delivery_period(
        datetime.datetime.now(), Currency.EUR, ["SE3"]
    )
    print(output)
```
