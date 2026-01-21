from typing import Optional

from dash import Input, Output, callback

from utils.converters import parse_date
from utils.formatters import format_date


@callback(Output("calendar-output", "children"), Input("calendar-picker", "date"))
def update_selected_date(value: Optional[str]) -> str:
    parsed = parse_date(value or "")
    if not parsed:
        return "Selecione uma data para visualizar detalhes."
    return f"Data escolhida: {format_date(parsed)}"
