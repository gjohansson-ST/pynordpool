"""Python API for Nord Pool."""

from __future__ import annotations

import asyncio
from datetime import datetime
from typing import Any

from aiohttp import (
    ClientError,
    ClientResponse,
    ClientResponseError,
    ClientSession,
    ClientTimeout,
    RequestInfo,
)

from .const import (
    API,
    AREAS,
    DEFAULT_TIMEOUT,
    HTTP_AUTH_FAILED_STATUS_CODES,
    LOGGER,
    Currency,
)
from .exceptions import (
    NordPoolAuthenticationError,
    NordPoolConnectionError,
    NordPoolEmptyResponseError,
    NordPoolError,
    NordPoolResponseError,
)
from .model import DeliveryPeriodBlockPrices, DeliveryPeriodData, DeliveryPeriodEntry
from .util import parse_datetime

__all__ = [
    "AREAS",
    "Currency",
    "DeliveryPeriodBlockPrices",
    "DeliveryPeriodData",
    "DeliveryPeriodEntry",
    "NordPoolAuthenticationError",
    "NordPoolClient",
    "NordPoolConnectionError",
    "NordPoolEmptyResponseError",
    "NordPoolError",
    "NordPoolResponseError",
]


class NordPoolClient:
    """Nord Pool client."""

    def __init__(
        self, session: ClientSession | None = None, timeout: int = DEFAULT_TIMEOUT
    ) -> None:
        """Initialize Nord Pool Client.

        session: aiohttp.ClientSession or None to create a new session.
        timeout: Timeout for API calls. Default is 8 seconds.
        """
        self._session = session if session else ClientSession()
        self._timeout = ClientTimeout(total=timeout)

    async def async_get_delivery_period(
        self,
        date: datetime,
        currency: Currency,
        areas: list[str],
        market: str = "DayAhead",
    ) -> DeliveryPeriodData:
        """Return info on delivery period data."""
        _date = datetime.strftime(date, "%Y-%m-%d")
        _currency = currency.value
        _market = market
        _areas = ",".join(areas)
        params = {
            "date": _date,
            "market": _market,
            "deliveryArea": _areas,
            "currency": _currency,
        }
        LOGGER.debug(
            "Retrieve prices from %s with params %s", API + "/DayAheadPrices", params
        )
        data = await self._get(API + "/DayAheadPrices", params)

        entries = []
        for entry in data["multiAreaEntries"]:
            entries.append(
                DeliveryPeriodEntry(
                    start=await parse_datetime(entry["deliveryStart"]),
                    end=await parse_datetime(entry["deliveryEnd"]),
                    entry=entry["entryPerArea"],
                )
            )
        block_prices = []
        for block in data["blockPriceAggregates"]:
            block_prices.append(
                DeliveryPeriodBlockPrices(
                    name=block["blockName"],
                    start=await parse_datetime(block["deliveryStart"]),
                    end=await parse_datetime(block["deliveryEnd"]),
                    average=block["averagePricePerArea"],
                )
            )

        area_averages: dict[str, float] = {}
        for area_average in data["areaAverages"]:
            area_averages[area_average["areaCode"]] = area_average["price"]

        return DeliveryPeriodData(
            raw=data,
            requested_date=data["deliveryDateCET"],
            updated_at=await parse_datetime(data["updatedAt"]),
            entries=entries,
            block_prices=block_prices,
            currency=data["currency"],
            exchange_rate=data["exchangeRate"],
            area_average=area_averages,
        )

    async def _get(
        self, path: str, params: dict[str, Any], retry: int = 3
    ) -> dict[str, Any]:
        """Make GET api call to Nord Pool api."""
        LOGGER.debug("Attempting get with path %s and parameters %s", path, params)
        try:
            async with self._session.get(
                path, params=params, timeout=self._timeout
            ) as resp:
                resp.raise_for_status()
                if resp.status == 204:
                    raise NordPoolEmptyResponseError(
                        "Status 204, Empty response from server"
                    )
                if resp.status != 200 and resp.status < 400:
                    error = await resp.text()
                    raise NordPoolResponseError(
                        request_info=RequestInfo(resp.url, resp.method, resp.headers),
                        history=(resp,),
                        status=resp.status,
                        message=error,
                    )
                return await self._response(resp)
        except NordPoolEmptyResponseError as error:
            LOGGER.debug("Empty response error %s", str(error))
            raise
        except NordPoolResponseError as error:
            LOGGER.debug("Response error %s", str(error))
            if retry > 0:
                await asyncio.sleep(7)
                return await self._get(path, params, retry - 1)
            raise
        except ClientResponseError as error:
            LOGGER.debug("Empty response error %s", str(error))
            if resp.status in HTTP_AUTH_FAILED_STATUS_CODES:
                raise NordPoolAuthenticationError("No access") from error
            if resp.status >= 500:
                raise NordPoolConnectionError("Internal server error") from error
            raise NordPoolResponseError(
                request_info=RequestInfo(resp.url, resp.method, resp.headers),
                history=(resp,),
                status=resp.status,
                message=str(error),
            ) from error
        except NordPoolConnectionError as error:
            LOGGER.debug("Connection error %s", str(error))
            if retry > 0:
                await asyncio.sleep(7)
                return await self._get(path, params, retry - 1)
            raise
        except ClientError as error:
            LOGGER.debug(
                "Retry %d on path %s from error %s", 4 - retry, path, str(error)
            )
            if retry > 0:
                await asyncio.sleep(7)
                return await self._get(path, params, retry - 1)
            raise NordPoolError from error

    async def _response(self, resp: ClientResponse) -> dict[str, Any]:
        """Return response from call."""
        LOGGER.debug("Response %s", resp.__dict__)
        LOGGER.debug("Response status %s", resp.status)
        response: dict[str, Any] = await resp.json()
        return response
