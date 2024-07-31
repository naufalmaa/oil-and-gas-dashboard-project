from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

# import plotly.express as px

from ...data.loader import LogDataSchema
from ...data.source import DataSource
from .. import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:
    # reset the parameter
    @app.callback(
        Output(ids.LITH_3D_FILTER, "value"),
        Input(ids.WELLS_LITH_3D_RESET_FILTER_BUTTON, "n_clicks"),
    )
    def reset_filter_graph_3d(n_clicks):
        reset_filter = "LITH"
        return reset_filter
    
    
    return [
        # choosing well name
        html.H5("Select Parameter 2", style={"marginTop": 10}),
        dmc.Select(
            placeholder="Select Parameter 2",
            id=ids.LITH_3D_FILTER,
            value ="LITH",
            data=[
                {'label': 'CALI', 'value': 'CALI'},
                {'label': 'RDEP', 'value': 'RDEP'},
                {'label': 'GR', 'value': 'GR'},
                {'label': 'RHOB', 'value': 'RHOB'},
                {'label': 'NPHI', 'value': 'NPHI'},
                {'label': 'SP', 'value': 'SP'},
                {'label': 'DTC', 'value': 'DTC'},
                {'label': 'Lithology', 'value': 'LITH'},
                {'label': 'Well', 'value': 'WELL_BORE_CODE'}
            ],
            style={"marginTop": 10},
            clearable=True,
            searchable=True,
            nothingFound="No Options Found",
        ),
        
        # reset-button
        dmc.Button(
            "Reset",
            id=ids.WELLS_LITH_3D_RESET_FILTER_BUTTON,
            variant="outline",
            color="dark",
            radius="10px",
            leftIcon=DashIconify(
                icon="material-symbols:restart-alt",
                width=25,
            ),
            style={"marginTop": "25px"},
        ),
    ]