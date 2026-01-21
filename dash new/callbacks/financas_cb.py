from dash import Input, Output, State, callback, html

from utils.converters import parse_float
from utils.formatters import format_currency


@callback(
    Output("financas-store", "data"),
    Input("financas-add", "n_clicks"),
    State("financas-descricao", "value"),
    State("financas-valor", "value"),
    State("financas-categoria", "value"),
    State("financas-store", "data"),
    prevent_initial_call=True,
)
def add_finance_entry(
    _clicks: int,
    descricao: str | None,
    valor: str | None,
    categoria: str | None,
    data: list[dict],
) -> list[dict]:
    if not descricao or not valor:
        return data
    item = {
        "descricao": descricao,
        "valor": parse_float(valor),
        "categoria": categoria or "Outros",
    }
    return [item, *data]


@callback(
    Output("financas-total", "children"),
    Output("financas-lista", "children"),
    Input("financas-store", "data"),
)
def render_finances(data: list[dict]) -> tuple[str, list[html.Li]]:
    total = sum(item.get("valor", 0.0) for item in data)
    items = [
        html.Li(
            f"{item.get('categoria')} - {item.get('descricao')}: "
            f"{format_currency(item.get('valor', 0.0))}"
        )
        for item in data
    ]
    return format_currency(total), items
