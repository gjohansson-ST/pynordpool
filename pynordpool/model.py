"""Data classes for Sensibo."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Any


@dataclass
class DeliveryPeriodData:
    """Dataclass for Delivery Period data."""

    raw: dict[str, Any]
    requested_date: str
    updated_at: datetime
    entries: list[DeliveryPeriodEntry]
    block_prices: list[DeliveryPeriodBlockPrices]
    currency: str
    exchange_rate: float
    area_average: dict[str, dict[str, float]]


@dataclass
class DeliveryPeriodEntry:
    """Dataclass for Delivery Period Entry."""

    start: datetime
    end: datetime
    entry: dict[str, float]


@dataclass
class DeliveryPeriodBlockPrices:
    """Dataclass for Delivery Period block prices."""

    name: str
    start: datetime
    end: datetime
    average: dict[str, dict[str, float]]
