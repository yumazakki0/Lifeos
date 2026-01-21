from dash import dcc, html
import dash
import dash_bootstrap_components as dbc

from componentes.header import render_header


dash.register_page(__name__, path="/tarefas")


layout = dbc.Container(
    fluid=True,
    children=[
        render_header("Tarefas", "Priorize o que importa"),
        dbc.Row(
            children=[
                dbc.Col(
                    [
                        dbc.Input(id="tarefas-input", placeholder="Nova tarefa"),
                        dbc.Button("Adicionar", id="tarefas-add", className="mt-2"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H5("Lista"),
                        html.Ul(id="tarefas-lista"),
                    ],
                    md=8,
                ),
            ]
        ),
        dcc.Store(id="tarefas-store", data=[]),
    ],
)
