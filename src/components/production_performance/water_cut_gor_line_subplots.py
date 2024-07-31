from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# import plotly.express as px

from ...data.loader import ProductionDataSchema
from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.WATER_CUT_GOR_SUBPLOTS, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER, "value"),
            Input(ids.TO_DATE_DATEPICKER, "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],
        prevent_initial_call=True,
    )
    def update_subplots(from_date: str, to_date: str, wells: list[str]) -> html.Div:
        if not wells:
            empty_fig = make_subplots(specs=[[{"secondary_y": True}]])
            empty_fig.update_layout(
                height=300,
                yaxis_title="Water Cut (%)",
                yaxis2_title="GOR (m3/m3)",
                margin=dict(l=10, r=10, t=10, b=10),
            )
            return html.Div(
                dcc.Graph(figure=empty_fig),
                id=ids.WATER_CUT_GOR_SUBPLOTS,
                className=cns.PPD_WATER_CUT_GOR_SUBPLOTS,
            )

        filtered_pt_cum_wc_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date_avg(ProductionDataSchema.WATER_CUT_DAILY)
        filtered_pt_cum_gor_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date_avg(ProductionDataSchema.GAS_OIL_RATIO)

        # Create subplots with two y-axes
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add water cut trace to the chart
        fig.add_trace(
            go.Scatter(
                x=filtered_pt_cum_wc_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_wc_date[ProductionDataSchema.WATER_CUT_DAILY],
                name="Water Cut",
                line=dict(color="darkgreen"),
            ),
            secondary_y=False,
        )

        # Add GOR trace to the chart
        fig.add_trace(
            go.Scatter(
                x=filtered_pt_cum_gor_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_gor_date[ProductionDataSchema.GAS_OIL_RATIO],
                name="GOR",
                line=dict(color="palevioletred"),
            ),
            secondary_y=True,
        )

        # Set y-axis titles
        fig.update_yaxes(
            title_text="Water Cut (%)",
            secondary_y=False,
            range=[-0.5, 10],
            title_font_size=12,
        )
        fig.update_yaxes(
            title_text="GOR (m\u00b3/m\u00b3)",
            secondary_y=True,
            range=[-0.5, 300],
            title_font_size=12,
        )

        fig.update_layout(
            template="plotly_white",
            height=300,
            autosize=True,  # Allow the figure to be autosized
            margin=dict(l=10, r=10, b=10),  # Adjust the margins for the figure
            legend=dict(
                x=0.5,  # Set the x position of the legend (0.5 means centered horizontally)
                y=1.2,  # Set the y position of the legend (1.0 means at the top)
                xanchor="center",  # Anchor point for the x position ('center' for center alignment)
                yanchor="top",  # Anchor point for the y position ('top' for top alignment)
                orientation="h",  # Orientation of the legend ('h' for horizontal)
                bgcolor="rgba(255, 255, 255, 0.5)",  # Background color of the legend (with transparency)
                # bordercolor='rgba(0, 0, 0, 0.5)',     # Border color of the legend (with transparency)
                # borderwidth=1       # Border width of the legend
            ),
            title={
                "text": "<b>Water Cut Daily and Gas Oil Ratio (GOR)</b>",
                "y": 0.88,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 24},
            },
        )

        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.WATER_CUT_GOR_SUBPLOTS,
            className=cns.PPD_WATER_CUT_GOR_SUBPLOTS,
        )

    return html.Div(
        id=ids.WATER_CUT_GOR_SUBPLOTS, className=cns.PPD_WATER_CUT_GOR_SUBPLOTS
    )
