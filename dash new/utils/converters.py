from __future__ import annotations

from datetime import datetime
from typing import Iterable, List, Optional


def parse_float(value: str) -> float:
    if not value:
        return 0.0
    normalized = value.replace(".", "").replace(",", ".")
    return float(normalized)


def to_list(values: Optional[Iterable[str]]) -> List[str]:
    return list(values or [])


def parse_date(value: str) -> Optional[datetime]:
    if not value:
        return None
    return datetime.fromisoformat(value)
