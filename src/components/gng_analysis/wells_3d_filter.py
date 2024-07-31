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
        Output(ids.WELLS_3D_FILTER, "value"),
        Input(ids.WELLS_LITH_3D_RESET_FILTER_BUTTON, "n_clicks"),
    )
    def reset_filter_graph_3d(n_clicks):
        reset_filter = "WELL_BORE_CODE"
        return reset_filter
    
    
    return [
        # choosing parameter
        html.H5("Select Parameter 1", style={"marginTop": 10}),
        dmc.Select(
            placeholder="Select Parameter 1",
            id=ids.WELLS_3D_FILTER,
            value ="WELL_BORE_CODE",
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
        
        # reset-button on lithology_distribution_3d_filter.py
    ]