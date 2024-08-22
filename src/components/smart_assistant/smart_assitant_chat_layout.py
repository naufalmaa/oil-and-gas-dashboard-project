from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import ids, cns

from ...data.source import DataSource

from . import smart_assitant_drawer

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        children=[
            smart_assitant_drawer.render(app, source)
        ]
    )