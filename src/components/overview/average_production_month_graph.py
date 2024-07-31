from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from ...data.loader import ProductionDataSchema, allBLOCKS, allWELLS
from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.AVG_PRODUCTION_MONTH_GRAPH, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.TO_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.BLOCK_MULTISELECT_FILTER_OVERVIEW, "value"),
        ],
        prevent_initial_call=True,
    )
    def update_line_chart(from_date: str, to_date: str, blocks: list[str]) -> html.Div:
        if not blocks:  # Check if the 'wells' list is empty
            # If there are no wells selected, return an empty plot
            empty_fig = make_subplots(specs=[[{"secondary_y": True}]])
            empty_fig.update_layout(
                template="plotly_white",
                title={
                    "text": "<b>Average Oil vs Gas Production per Month</b>",
                    "y": 0.95,
                    "x": 0.5,
                    "xanchor": "center",
                    "yanchor": "top",
                    "font": {"size": 24},
                },
                # height=300,
                autosize=True,  # Allow the figure to be autosized
                margin=dict(l=10, r=10, b=10),  # Adjust the margins for the figure
                legend=dict(
                    x=0.25,  # Set the x position of the legend (0.5 means centered horizontally)
                    y=1.175,  # Set the y position of the legend (1.0 means at the top)
                    xanchor="center",  # Anchor point for the x position ('center' for center alignment)
                    yanchor="top",  # Anchor point for the y position ('top' for top alignment)
                    orientation="h",  # Orientation of the legend ('h' for horizontal)
                    bgcolor="rgba(255, 255, 255, 0.5)",  # Background color of the legend (with transparency)
                    # bordercolor='rgba(0, 0, 0, 0.5)',     # Border color of the legend (with transparency)
                    # borderwidth=1       # Border width of the legend
                ),
            )

            return html.Div(
                dcc.Graph(figure=empty_fig),
                id=ids.AVG_PRODUCTION_MONTH_GRAPH,
                className=cns.OVW_AVG_PRODUCTION_MONTH_GRAPH,
            )

        # for productions
        filtered_source_production = source.filter_overview(
            from_date=from_date, to_date=to_date, blocks=blocks
        ).df_production

        filtered_df = source.create_table_prod_mth(
            df=filtered_source_production,
            type="avg"
        )
        
        fig = make_subplots(
            specs=[
                [{"secondary_y": True}]
            ],
        )

        # Add traces for BORE_OIL_VOL in barrels on row 1 col 1
        fig.add_trace(
            go.Scatter(
                name="Average Oil Volume per Month (in Barrels Oil)",
                x=filtered_df["Year_Month"],
                y=filtered_df["BORE_OIL_VOL_barrels"],
                mode="lines",
                # line={},
                line=dict(color=px.colors.qualitative.Safe[0]),
                showlegend=True,
            ),
            secondary_y=False,
        )

        # Add traces for BORE_GAS_VOL in MCF on row 1 col 1
        fig.add_trace(
            go.Scatter(
                x=filtered_df["Year_Month"],
                y=filtered_df["BORE_GAS_VOL_MCF"],
                name="Average Gas Volume per Month (in MCF)",
                mode="lines",
                # line={},
                line=dict(color=px.colors.qualitative.Safe[1]),
                showlegend=True,
            ),
            secondary_y=True,
        )

        # Update layout
        fig.update_layout(
            template="plotly_white",
            title={
                "text": "<b>Average Oil vs Gas Production per Month</b>",
                "y": 0.95,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 24},
            },
            # height=300,
            autosize=True,  # Allow the figure to be autosized
            margin=dict(l=10, r=10, b=10),  # Adjust the margins for the figure
            legend=dict(
                x=0.5,  # Set the x position of the legend (0.5 means centered horizontally)
                y=1.15,  # Set the y position of the legend (1.0 means at the top)
                xanchor="center",  # Anchor point for the x position ('center' for center alignment)
                yanchor="top",  # Anchor point for the y position ('top' for top alignment)
                orientation="h",  # Orientation of the legend ('h' for horizontal)
                bgcolor="rgba(255, 255, 255, 0.5)",  # Background color of the legend (with transparency)
                # bordercolor='rgba(0, 0, 0, 0.5)',     # Border color of the legend (with transparency)
                # borderwidth=1       # Border width of the legend
            ),
        )

        # Update y-axis labels
        fig.update_yaxes(title_text="Oil Volume (in Barrels Oil)", secondary_y=False, range=[0, 30000])
        fig.update_yaxes(title_text="Gas Volume (in MCF)",secondary_y=True, range=[0, 30e9])

        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.AVG_PRODUCTION_MONTH_GRAPH,
            className=cns.OVW_AVG_PRODUCTION_MONTH_GRAPH,
        )

    return html.Div(
        id=ids.AVG_PRODUCTION_MONTH_GRAPH, className=cns.OVW_AVG_PRODUCTION_MONTH_GRAPH
    )
