from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import ids, cns

from ...data.source import DataSource

from ..Zara_Assistant import Zara_Drawer

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        children=[
            Zara_Drawer.render(app, source)
        ]
    )