[![size_badge](https://img.shields.io/github/repo-size/gjohansson-ST/pynordpool?style=for-the-badge&cacheSeconds=3600)](https://github.com/gjohansson-ST/pynordpool)
[![version_badge](https://img.shields.io/github/v/release/gjohansson-ST/pynordpool?label=Latest%20release&style=for-the-badge&cacheSeconds=3600)](https://github.com/gjohansson-ST/pynordpool/releases/latest)
[![download_badge](https://img.shields.io/pypi/dm/pynordpool?style=for-the-badge&cacheSeconds=3600)](https://github.com/gjohansson-ST/pynordpool/releases/latest)
![GitHub Repo stars](https://img.shields.io/github/stars/gjohansson-ST/pynordpool?style=for-the-badge&cacheSeconds=3600)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/gjohansson-ST/pynordpool?style=for-the-badge&cacheSeconds=3600)
![GitHub License](https://img.shields.io/github/license/gjohansson-ST/pynordpool?style=for-the-badge&cacheSeconds=3600)

[![Made for Home Assistant](https://img.shields.io/badge/Made_for-Home%20Assistant-blue?style=for-the-badge&logo=homeassistant)](https://github.com/home-assistant)

[![Sponsor me](https://img.shields.io/badge/Sponsor-Me-blue?style=for-the-badge&logo=github)](https://github.com/sponsors/gjohansson-ST)
![Discord](https://img.shields.io/discord/872446427664625664?style=for-the-badge&label=Discord&cacheSeconds=3600)

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
