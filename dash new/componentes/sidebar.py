from dash import html
import dash_bootstrap_components as dbc


def render_sidebar() -> html.Div:
    links = [
        ("Dashboard", "/"),
        ("Calendário", "/calendario"),
        ("Finanças", "/financas"),
        ("Diário", "/diario"),
        ("Tarefas", "/tarefas"),
    ]

    return html.Div(
        className="sidebar",
        children=[
            html.H4("LifeOS", className="px-3 pt-3"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink(label, href=path, active="exact")
                    for label, path in links
                ],
                vertical=True,
                pills=True,
            ),
        ],
    )
