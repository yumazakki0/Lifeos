from datetime import date

from data.models import FinanceEntry, JournalEntry, Task


def seed_tasks() -> list[Task]:
    return [
        Task(title="Planejar a semana"),
        Task(title="Revisar orçamento", done=True),
        Task(title="Ler 20 páginas"),
    ]


def seed_journal() -> list[JournalEntry]:
    return [
        JournalEntry(day=date.today(), text="Hoje foquei em hábitos melhores."),
    ]


def seed_finances() -> list[FinanceEntry]:
    return [
        FinanceEntry(category="Alimentação", amount=58.9, description="Mercado"),
        FinanceEntry(category="Transporte", amount=22.5, description="App de transporte"),
    ]
