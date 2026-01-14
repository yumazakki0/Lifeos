from dash import Dash, html
import dash_bootstrap_components as dbc
import dash

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

server = app.server

app.layout = html.Div(
    className="app-container",
    children=[
        # Sidebar fixa (entra depois)
        html.Div(id="sidebar"),

        # Conteúdo das páginas
        html.Div(
            className="content",
            children=dash.page_container
        )
    ]
)

from pages.dashboard import *
#importe de precaução de callbacks para evitar erro de susteem do codigo por ser resumido nas pages
from callback.dashboard_cb import *
from callback.calendario_cb import *
from callback.financas_cb import *
from callback.diario_cb import *
from callback.tarefas_cb import *


if __name__ == "__main__":
    app.run(debug=True)

