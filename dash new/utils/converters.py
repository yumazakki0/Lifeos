from __future__ import annotations

from datetime import datetime
from typing import Iterable


def parse_float(value: str) -> float:
    if not value:
        return 0.0
    normalized = value.replace(".", "").replace(",", ".")
    return float(normalized)


def to_list(values: Iterable[str] | None) -> list[str]:
    return list(values or [])


def parse_date(value: str) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value)
