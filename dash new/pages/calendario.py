from dash import dcc, html
import dash
import dash_bootstrap_components as dbc

from componentes.header import render_header


dash.register_page(__name__, path="/calendario")


layout = dbc.Container(
    fluid=True,
    children=[
        render_header("Calendário", "Planeje seus compromissos"),
        dbc.Row(
            children=[
                dbc.Col(
                    [
                        html.Label("Selecione a data"),
                        dcc.DatePickerSingle(id="calendar-picker"),
                        html.Div(id="calendar-output", className="mt-2 text-muted"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    dbc.Alert(
                        "Use esta área para listar compromissos e objetivos da semana.",
                        color="info",
                    ),
                    md=8,
                ),
            ]
        ),
    ],
)
