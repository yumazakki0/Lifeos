from dash import html
import dash_bootstrap_components as dbc

from utils.constants import APP_TITLE


def render_header(title: str | None = None, subtitle: str | None = None) -> dbc.Container:
    return dbc.Container(
        className="py-4",
        children=[
            html.H2(title or APP_TITLE, className="mb-1"),
            html.P(subtitle or "Organize sua vida com foco no essencial.", className="text-muted"),
        ],
    )
