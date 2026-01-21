from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    done: bool = False


@dataclass
class JournalEntry:
    day: date
    text: str


@dataclass
class FinanceEntry:
    category: str
    amount: float
    description: str
