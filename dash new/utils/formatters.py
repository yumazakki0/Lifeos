from __future__ import annotations

from datetime import datetime

from utils.constants import DEFAULT_CURRENCY, DEFAULT_DATE_FORMAT


def format_currency(value: float, currency: str = DEFAULT_CURRENCY) -> str:
    return f"{currency} {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_date(value: datetime, date_format: str = DEFAULT_DATE_FORMAT) -> str:
    return value.strftime(date_format)
