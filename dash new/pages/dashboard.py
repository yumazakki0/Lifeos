from dash import dcc, html
import dash
import dash_bootstrap_components as dbc

from componentes.cards import summary_card
from componentes.header import render_header
from componentes.tables import simple_table
from data.seed import seed_tasks


dash.register_page(__name__, path="/")


layout = dbc.Container(
    fluid=True,
    children=[
        render_header("Dashboard", "Visão geral do seu dia"),
        dbc.Row(
            className="g-3",
            children=[
                dbc.Col(summary_card("Tarefas pendentes", "3", "Atualizado agora"), md=4),
                dbc.Col(summary_card("Rotina", "2 hábitos", "Próximo check-in"), md=4),
                dbc.Col(summary_card("Gastos hoje", "R$ 81,40", "Limite diário"), md=4),
            ],
        ),
        html.Hr(),
        html.H5("Tarefas rápidas"),
        simple_table(
            ["Atividade", "Status"],
            [[task.title, "Feita" if task.done else "Pendente"] for task in seed_tasks()],
        ),
        dcc.Interval(id="dashboard-tick", interval=30_000, n_intervals=0),
        html.Small(id="dashboard-last-update", className="text-muted"),
    ],
)
