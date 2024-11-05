"""Constants for Nordpool."""

from __future__ import annotations

import datetime as dt
import logging
from enum import StrEnum

API = "https://dataportal-api.nordpoolgroup.com/api"

LOGGER = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 8
HTTP_AUTH_FAILED_STATUS_CODES = {401, 403}
DEFAULT_TIME_ZONE: dt.tzinfo = dt.UTC

AREAS = {
    # Baltics
    "EE": "Estonia",
    "LT": "Lithuania",
    "LV": "Latvia",
    # CWE
    "AT": "Austria",
    "BE": "Belgium",
    "FR": "France",
    "GER": "Germany",
    "NL": "Netherlands",
    "PL": "Poland",
    # Nordic
    "DK1": "Denmark 1",
    "DK2": "Denmark 2",
    "FI": "Finland",
    "NO1": "Norway 1",
    "NO2": "Norway 2",
    "NO3": "Norway 3",
    "NO4": "Norway 4",
    "NO5": "Norway 5",
    "SE1": "Sweden 1",
    "SE2": "Sweden 2",
    "SE3": "Sweden 3",
    "SE4": "Sweden 4",
    # System
    "SYS": "System price",
}


class Currency(StrEnum):
    """Currency picker."""

    DKK = "DKK"
    EUR = "EUR"
    NOK = "NOK"
    PLN = "PLN"
    SEK = "SEK"
