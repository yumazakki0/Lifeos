from dash import Dash, html
import dash
import dash_bootstrap_components as dbc

from componentes.sidebar import render_sidebar
import pages.dashboard  # noqa: F401
import pages.calendario  # noqa: F401
import pages.financas  # noqa: F401
import pages.diario  # noqa: F401
import pages.tarefas  # noqa: F401

import callbacks.dashboard_cb  # noqa: F401
import callbacks.calendario_cb  # noqa: F401
import callbacks.financas_cb  # noqa: F401
import callbacks.diario_cb  # noqa: F401
import callbacks.tarefas_cb  # noqa: F401

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

server = app.server

app.layout = html.Div(
    className="app-container d-flex",
    children=[
        render_sidebar(),
        html.Div(
            className="content flex-grow-1 p-4",
            children=dash.page_container,
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
