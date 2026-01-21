from typing import List

import dash_bootstrap_components as dbc
from dash import html


def simple_table(headers: List[str], rows: List[List[str]]) -> dbc.Table:
    return dbc.Table(
        bordered=False,
        hover=True,
        responsive=True,
        striped=True,
        children=[
            html.Thead(html.Tr([html.Th(h) for h in headers])),
            html.Tbody(
                [html.Tr([html.Td(cell) for cell in row]) for row in rows]
            ),
        ],
    )
