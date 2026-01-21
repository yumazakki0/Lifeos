from typing import Optional

import dash_bootstrap_components as dbc
from dash import html


def summary_card(title: str, value: str, helper: Optional[str] = None) -> dbc.Card:
    return dbc.Card(
        className="shadow-sm",
        body=True,
        children=[
            html.P(title, className="text-muted mb-1"),
            html.H4(value, className="mb-0"),
            html.Small(helper, className="text-muted") if helper else None,
        ],
    )
