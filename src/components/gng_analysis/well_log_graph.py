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
        Output(component_id=ids.WELL_LOG_FIRST_GRAPH, component_property="children"),
        [
            Input(component_id=ids.WELL_LOG_SELECT, component_property="value"),
            Input(component_id=ids.WELL_LOG_PARAMETER_CHECKBOX, component_property="value"),
        ],
        prevent_initial_call=True,
    )
    def build_graph(well_chosen, params_chosen):
        # # 'Well-E1' 'Well-N1' 'Well-W1' 'Well-C1' 'Well-S1' 'Well-N2' 'Well-E2' 'Well-W2' 'Well-E3'
        # dataframe_log_data = {
        #                 'well1': well1,
        #                 'well2': well2,
        #                 'well3': well3,
        #                 'well4': well4,
        #                 'well5': well5,
        #                 'well6': well6,
        #                 'well7': well7,
        #                 'well8': well8,
        #                 'well9': well9
        #             }

        # # define colors
        # colors = ['black', 'firebrick', 'green', 'mediumaquamarine', 'royalblue', 'goldenrod', 'lightcoral']

        # figure_column = np.arange(1, 1+len(params_chosen))

        if params_chosen is not None:
            filtered_well_log_data = source.filter_log(
                wells=well_chosen, params=params_chosen
            ).to_dataframe

            all_parameters = source.unique_params_log

            # Generate a list of colors for all parameters
            colors = [
                "rgb(136, 204, 238)",
                "rgb(204, 102, 119)",
                "rgb(221, 204, 119)",
                "rgb(17, 119, 51)",
                "rgb(51, 34, 136)",
                "rgb(170, 68, 153)",
                "rgb(68, 170, 153)",
            ]  # You can use any color palette

            # Create an empty list to store the traces
            traces = []

            # Iterate through all parameters, even if not selected
            for i, param in enumerate(all_parameters):
                # Check if the parameter is selected
                if param in params_chosen:
                    # Get the data for the selected parameter
                    data = filtered_well_log_data[param]

                    # Create a scatter trace and append to the list of traces
                    trace = go.Scatter(
                        x=data,
                        y=filtered_well_log_data[LogDataSchema.DEPTH],
                        name=param,
                        line=dict(color=colors[i]),  # Set the color
                    )
                    traces.append(trace)
                else:
                    # Create an empty trace for parameters not selected
                    trace = go.Scatter(x=[], y=[], name="empty")
                    traces.append(trace)

            # Create the figure with subplots and add the traces
            figure = make_subplots(
                rows=1,
                cols=len(all_parameters),
                shared_yaxes=True,
                subplot_titles=all_parameters,
                column_widths=[400] * len(all_parameters),
            )

            for i, trace in enumerate(traces):
                figure.add_trace(trace, row=1, col=i + 1)
                figure.update_xaxes(
                    type="log",
                    row=1,
                    col=i + 1,
                    # title_text=params_chosen[i],
                    tickfont_size=12,
                    linecolor="#585858",
                )

            # Update x-axes properties
            figure.update_xaxes(
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                ticks="inside",
                tickangle=0,
            )

            # Update y-axes properties
            figure.update_yaxes(
                range=[3300, 400],
                tickmode="linear",
                tick0=0,
                dtick=250,
                showline=True,
                linewidth=2,
                linecolor="black",
                mirror=True,
                ticks="outside",
            )

            # Update layout properties
            figure.update_layout(
                title=well_chosen,
                height=750,
                showlegend=False,
                # xaxis_range=[x_min, x_max],  # Set desired x range
                # yaxis_range=[y_min, y_max],  # Set desired y range
            )

            return (
                html.Div(  # graph for well-log data
                    dcc.Graph(figure=figure),
                    id=ids.WELL_LOG_FIRST_GRAPH,
                    className=cns.GNG_WELL_LOG_GRAPHS,
                ),
            )

        else:
            pass

    return html.Div(
        id=ids.WELL_LOG_FIRST_GRAPH,
        className=cns.GNG_WELL_LOG_GRAPHS,
        # children=[
        #     html.H1(
        #         "Well-Log Graph",
        #         id="title-graph-well-log",
        #         style={"marginTop": 10, "paddingLeft": 10},
        #     ),
        #     # graph for well-log data
        #     dcc.Graph(
        #         id="output-graph-well-log", className=cns.WL_FIRST_GRAPH, figure={}
        #     ),
        #     html.Br(),
        # ],
    )
