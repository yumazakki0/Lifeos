from dash import dcc, html
import dash
import dash_bootstrap_components as dbc

from componentes.header import render_header


dash.register_page(__name__, path="/financas")


layout = dbc.Container(
    fluid=True,
    children=[
        render_header("Finanças", "Controle entradas e saídas"),
        dbc.Row(
            className="g-3",
            children=[
                dbc.Col(
                    [
                        dbc.Input(id="financas-descricao", placeholder="Descrição"),
                        dbc.Input(
                            id="financas-valor",
                            placeholder="Valor (ex: 120,00)",
                            className="mt-2",
                        ),
                        dbc.Select(
                            id="financas-categoria",
                            options=[
                                {"label": "Alimentação", "value": "Alimentação"},
                                {"label": "Transporte", "value": "Transporte"},
                                {"label": "Lazer", "value": "Lazer"},
                            ],
                            className="mt-2",
                        ),
                        dbc.Button("Adicionar", id="financas-add", className="mt-2"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H5("Resumo"),
                        html.Div(id="financas-total", className="display-6"),
                        html.Ul(id="financas-lista"),
                    ],
                    md=8,
                ),
            ],
        ),
        dcc.Store(id="financas-store", data=[]),
    ],
)
