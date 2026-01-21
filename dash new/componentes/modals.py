import dash_bootstrap_components as dbc
from dash import html


def info_modal(modal_id: str, title: str, body: str) -> dbc.Modal:
    return dbc.Modal(
        id=modal_id,
        is_open=False,
        children=[
            dbc.ModalHeader(dbc.ModalTitle(title)),
            dbc.ModalBody(html.P(body)),
            dbc.ModalFooter(
                dbc.Button("Fechar", id=f"{modal_id}-close", className="ms-auto")
            ),
        ],
    )
