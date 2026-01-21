from datetime import datetime

from dash import Input, Output, callback

from utils.formatters import format_date


@callback(Output("dashboard-last-update", "children"), Input("dashboard-tick", "n_intervals"))
def update_dashboard_timestamp(_: int) -> str:
    return f"Última atualização: {format_date(datetime.now())}"
