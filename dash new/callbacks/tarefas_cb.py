from typing import List, Optional

from dash import Input, Output, State, callback, html


@callback(
    Output("tarefas-store", "data"),
    Input("tarefas-add", "n_clicks"),
    State("tarefas-input", "value"),
    State("tarefas-store", "data"),
    prevent_initial_call=True,
)
def add_task(_clicks: int, value: Optional[str], data: List[str]) -> List[str]:
    if not value:
        return data
    return [value, *data]


@callback(Output("tarefas-lista", "children"), Input("tarefas-store", "data"))
def render_tasks(data: List[str]) -> List[html.Li]:
    if not data:
        return [html.Li("Nenhuma tarefa cadastrada.")]
    return [html.Li(task) for task in data]
