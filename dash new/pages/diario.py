from dash import dcc, html
import dash
import dash_bootstrap_components as dbc

from componentes.header import render_header


dash.register_page(__name__, path="/diario")


layout = dbc.Container(
    fluid=True,
    children=[
        render_header("Diário", "Registre reflexões do dia"),
        dbc.Row(
            children=[
                dbc.Col(
                    [
                        dcc.Textarea(
                            id="diario-texto",
                            placeholder="Como foi o seu dia?",
                            style={"width": "100%", "minHeight": "180px"},
                        ),
                        dbc.Button("Salvar", id="diario-salvar", className="mt-2"),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.H5("Última anotação"),
                        html.Div(id="diario-ultima", className="text-muted"),
                    ],
                    md=6,
                ),
            ]
        ),
        dcc.Store(id="diario-store", data=""),
    ],
)
