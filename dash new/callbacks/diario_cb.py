from dash import Input, Output, State, callback


@callback(
    Output("diario-store", "data"),
    Input("diario-salvar", "n_clicks"),
    State("diario-texto", "value"),
    prevent_initial_call=True,
)
def save_journal(_clicks: int, texto: str | None) -> str:
    return texto or ""


@callback(Output("diario-ultima", "children"), Input("diario-store", "data"))
def show_last_entry(texto: str) -> str:
    if not texto:
        return "Nenhuma anotação salva ainda."
    return texto
