# pynordpool
python module for communicating with Nord Pool

Development and testing done with 3.11

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
