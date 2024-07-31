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
        Output(ids.OPERATOR_WELL_COUNTS_PIE_CHART, "children"),
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
                id=ids.OPERATOR_WELL_COUNTS_PIE_CHART,
                className=cns.OVW_OPERATOR_WELL_COUNTS_PIE_CHART,
            )
        
        # for operator count
        filter_unique_blocks = source.filter_overview(
            from_date=from_date, to_date=to_date, blocks=blocks
        ).unique_blocks
        
        gdf_blocks = source.gdf_blocks
        condition_gdf_blocks = gdf_blocks[gdf_blocks[allBLOCKS.BLOCK_NAME].isin(filter_unique_blocks)]
        
        # for wells count
        gdf_wells = source.gdf_wells
        condition_gdf_wells = gdf_wells[gdf_wells[allWELLS.BLOCK_WELL].isin(filter_unique_blocks)]
        


        fig = make_subplots(
            rows=1,
            cols=2,
            # column_widths=[0.7, 0.3],
            # row_heights=[0.5, 0.5],
            specs=[
                [{"type": "pie"}, {"type": "pie"}],
            ],
            subplot_titles=(
                "<b>Operators Count</b>",
                "<b>Well Counts by Purpose</b>"
            ),
        )
        
        # Add Pie Chart for operator counts
        fig.add_trace(
            go.Pie(
                name="Operator Counts",
                # title_text="<b>Operators Count</b><br>&nbsp;",
                # title_position="top center",
                # title_font_size=24,
                labels=condition_gdf_blocks[
                    allBLOCKS.OPERATOR_BLOCK
                ].value_counts().index.to_list(),
                values=condition_gdf_blocks[
                    allBLOCKS.OPERATOR_BLOCK
                ].value_counts().to_list(),
                # hole=0.5,
                customdata=condition_gdf_blocks[
                    allBLOCKS.BLOCK_NAME
                ].to_list(),
                
                marker=dict(colors=px.colors.sequential.RdBu),
                
            ),
            row=1,
            col=1,
        )
        
        # Add Pie Chart for well counts
        fig.add_trace(
            go.Pie(
                name="Well Counts by Purpose",
                # title_text="<b>Well Counts by Purpose</b><br>&nbsp;",
                # title_position="top center",
                # title_font_size=24,
                labels=condition_gdf_wells[
                    allWELLS.PURPOSE_WELL
                ].value_counts().index.to_list(),
                values=condition_gdf_wells[
                    allWELLS.PURPOSE_WELL
                ].value_counts().to_list(),
                # hole=0.5,
                customdata=[
                    "Well-E1, Well-N1, Well-W1, Well-C1, Well-S1",
                    "Well-N2, Well-W2",
                    "Well-E2",
                    "Well-E3"
                ],
                marker=dict(colors=px.colors.sequential.Aggrnyl),

            ),
            row=1,
            col=2,
        )
        
        fig.update_traces(
            textposition='inside',
            hovertemplate='Operator: %{label}<br>Value:%{value}<br>Block-Name: %{customdata}<extra></extra>',
            row=1,
            col=1,
        )

        fig.update_traces(
            # textinfo='value',
            textposition='inside',
            hovertemplate='Purposes: %{label}<br>Value:%{value}<br>Wells: %{customdata}<extra></extra>',
            row=1,
            col=2,
        )

        # Update layout
        fig.update_layout(
            template="plotly_white",
            height=300,
            # width=300,
            autosize=True,  # Allow the figure to be autosized
            margin=dict(l=10, r=10, b=10),  # Adjust the margins for the figure
            # legend=dict(
            #     x=0.5,  # Set the x position of the legend (0.5 means centered horizontally)
            #     y=1.15,  # Set the y position of the legend (1.0 means at the top)
            #     xanchor="center",  # Anchor point for the x position ('center' for center alignment)
            #     yanchor="top",  # Anchor point for the y position ('top' for top alignment)
            #     orientation="h",  # Orientation of the legend ('h' for horizontal)
            #     bgcolor="rgba(255, 255, 255, 0.5)",  # Background color of the legend (with transparency)
            #     # bordercolor='rgba(0, 0, 0, 0.5)',     # Border color of the legend (with transparency)
            #     # borderwidth=1       # Border width of the legend
            # ),
        )

        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.OPERATOR_WELL_COUNTS_PIE_CHART,
            className=cns.OVW_OPERATOR_WELL_COUNTS_PIE_CHART,
        )

    return html.Div(
        id=ids.OPERATOR_WELL_COUNTS_PIE_CHART, className=cns.OVW_OPERATOR_WELL_COUNTS_PIE_CHART
    )