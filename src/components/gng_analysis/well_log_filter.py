from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify
from dash.exceptions import PreventUpdate

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# import plotly.express as px

from ...data.loader import LogDataSchema
from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    # reset the well-log parameter
    @app.callback(
        Output(ids.WELL_LOG_PARAMETER_CHECKBOX, "value"),
        Input(ids.WELL_LOG_RESET_FILTER_BUTTON, "n_clicks"),
    )
    def reset_filter_well_log(n_clicks) -> html.Div:
        # if n_clicks is None:
        #     raise PreventUpdate
        # else:
            reset_filter = source.unique_params_log
            return reset_filter

    return [
        # choosing well name
        html.H5("Well Name", style={"marginTop": 10}),
        dmc.Select(
            placeholder="Select Borehole Name",
            id=ids.WELL_LOG_SELECT,
            value ="Well-E1",
            data=[
                #   'Well-E1' 'Well-N1' 'Well-W1' 'Well-C1' 'Well-S1' 'Well-N2' 'Well-E2' 'Well-W2' 'Well-E3'
                {
                    "label": "Well-E1",
                    "value": "Well-E1",
                },
                {
                    "label": "Well-N1",
                    "value": "Well-N1",
                },
                {
                    "label": "Well-W1",
                    "value": "Well-W1",
                },
                {
                    "label": "Well-C1",
                    "value": "Well-C1",
                },
                {
                    "label": "Well-S1",
                    "value": "Well-S1",
                },
                {
                    "label": "Well-N2",
                    "value": "Well-N2",
                },
                {
                    "label": "Well-E2",
                    "value": "Well-E2",
                },
                {
                    "label": "Well-W2",
                    "value": "Well-W2",
                },
                {
                    "label": "Well-E3",
                    "value": "Well-E3",
                },
            ],
            style={"marginTop": 10},
            clearable=True,
            searchable=True,
            nothingFound="No Options Found",
        ),
        # choosing well-log parameter to show
        html.H5(
            "Well-Log Parameter",
            style={"marginTop": 30},
        ),
        dmc.CheckboxGroup(
            id=ids.WELL_LOG_PARAMETER_CHECKBOX,
            orientation="vertical",
            children=[
                # ['CALI','RDEP','GR','RHOB','NPHI','SP','DTC']
                dmc.Checkbox(
                    label="CALI",
                    value="CALI",
                    color="dark",
                    style={"marginTop": 0},
                ),
                dmc.Checkbox(
                    label="RDEP",
                    value="RDEP",
                    color="dark",
                    style={"marginTop": -15},
                ),
                dmc.Checkbox(
                    label="GR",
                    value="GR",
                    color="dark",
                    style={"marginTop": -15},
                ),
                dmc.Checkbox(
                    label="RHOB",
                    value="RHOB",
                    color="dark",
                    style={"marginTop": -15},
                ),
                dmc.Checkbox(
                    label="NPHI",
                    value="NPHI",
                    color="dark",
                    style={"marginTop": -15},
                ),
                dmc.Checkbox(
                    label="SP",
                    value="SP",
                    color="dark",
                    style={"marginTop": -15},
                ),
                dmc.Checkbox(
                    label="DTC",
                    value="DTC",
                    color="dark",
                    style={"marginTop": -15},
                ),
            ],
            # value=[
            #     "CALI",
            #     "RDEP",
            #     "GR",
            #     "RHOB",
            #     "NPHI",
            #     "SP",
            #     "DTC",
            # ],
            value=source.unique_params_log,
        ),
        # reset-button
        dmc.Button(
            "Reset",
            id=ids.WELL_LOG_RESET_FILTER_BUTTON,
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
