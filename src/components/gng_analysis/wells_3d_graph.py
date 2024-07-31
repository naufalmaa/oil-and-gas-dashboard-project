from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# import plotly.express as px

from ...data.loader import LogDataSchema
from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(component_id=ids.WELLS_3D_GRAPH, component_property="children"),
        [Input(component_id=ids.WELLS_3D_FILTER, component_property="value")],
    )
    def update_3d_graph(params_chosen):
        wells_3d_data = source.df_log
        
        # if params_chosen is not None:
        
        figure = px.scatter_3d(
            wells_3d_data,
            x=LogDataSchema.X,
            y=LogDataSchema.Y,
            z=LogDataSchema.Z,
            color=params_chosen,
            color_continuous_scale=px.colors.sequential.Aggrnyl,
            color_discrete_sequence=px.colors.qualitative.Safe,
        )
        
        # figure.update_layout()
    
        return html.Div(
            dcc.Graph(figure=figure),
            id=ids.WELLS_3D_GRAPH,
            className=cns.GNG_WELLS_3D_GRAPH,
        )
        # else:
        #     pass

    return html.Div(
        id=ids.WELLS_3D_GRAPH,
        className=cns.GNG_WELLS_3D_GRAPH,
    )
