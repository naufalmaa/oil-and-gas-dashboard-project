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
        Output(ids.OIL_VS_WATER_SUBPLOTS, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER, "value"),
            Input(ids.TO_DATE_DATEPICKER, "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],
        prevent_initial_call=True,
    )
    def update_subplots(from_date: str, to_date: str, wells: list[str]) -> html.Div:
        if not wells:
            empty_fig = make_subplots(rows=1, cols=1)
            empty_fig.update_layout(
                height=300,
                margin=dict(l=10, r=10, t=10, b=10),
            )
            return html.Div(
                dcc.Graph(figure=empty_fig),
                id=ids.OIL_VS_WATER_SUBPLOTS,
                className=cns.PPD_OIL_VS_WATER_SUBPLOTS,
            )

        filtered_pt_oil_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date(ProductionDataSchema.BORE_OIL_VOL)
        filtered_pt_wtr_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date(ProductionDataSchema.BORE_WAT_VOL)

        filtered_pt_choke_size_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date(ProductionDataSchema.DP_CHOKE_SIZE)
        filtered_pt_avg_dp_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date(ProductionDataSchema.AVG_DOWNHOLE_PRESSURE)

        # Initialize figure with subplots
        figure = make_subplots(
            rows=1,
            cols=2,
            # column_widths=[0.5, 0.5],
            subplot_titles=(
                "<b>Oil and Water Total Rate by Time</b>",
                "<b>Choke Size and Avg Downhole Pressure</b>",
            ),
            # row_heights=[0.5, 0.5],
            specs=[
                [{"type": "scatter"}, {"type": "scatter"}],
            ],
        )

        # line chart for BORE_OIL_VOL
        figure.add_trace(
            go.Scatter(
                name="Total Oil Volume",
                x=filtered_pt_oil_date[ProductionDataSchema.DATE],
                y=filtered_pt_oil_date[ProductionDataSchema.BORE_OIL_VOL],
                mode="lines",
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                # fillpattern={'fillmode':'overlay', 'fgcolor':'rgb(3,166,166, 0.0001)'},
                line={"color": "#f2b705", "width": 1},
                showlegend=True,
            ),
            row=1,
            col=1,
        )

        # line chart for BORE_WAT_VOL
        figure.add_trace(
            go.Scatter(
                name="Total Water Volume",
                x=filtered_pt_wtr_date[ProductionDataSchema.DATE],
                y=filtered_pt_wtr_date[ProductionDataSchema.BORE_WAT_VOL],
                mode="lines",
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                # fillpattern={'fillmode':'overlay', 'fgcolor':'rgb(3,166,166, 0.0001)'},
                line={"color": "#03a6a6", "width": 1},
                showlegend=True,
            ),
            row=1,
            col=1,
        )

        figure.add_trace(
            go.Scatter(
                name="Total Downhole Pressure Choke Size",
                x=filtered_pt_choke_size_date[ProductionDataSchema.DATE],
                y=filtered_pt_choke_size_date[ProductionDataSchema.DP_CHOKE_SIZE],
                mode="lines",
                line={"color": "tomato", "width": 1},
                showlegend=True,
            ),
            row=1,
            col=2,
        )

        # line chart for AVG_DOWNHOLE_PRESSURE
        figure.add_trace(
            go.Scatter(
                name="Total Avg Downhole Pressure",
                x=filtered_pt_avg_dp_date[ProductionDataSchema.DATE],
                y=filtered_pt_avg_dp_date[ProductionDataSchema.AVG_DOWNHOLE_PRESSURE],
                mode="lines",
                line={"color": "violet", "width": 1},
                showlegend=True,
            ),
            row=1,
            col=2,
        )

        # Set theme, margin, and annotation in layout
        # figure.update_layout(
        #     title='<b>Oil and Water Total Rate by Time (Yearly, Monthly, Daily)</b>',
        #     xaxis_title='Date'
        # )

        # Set y-axis titles
        figure.update_yaxes(
            title_text="Total Vol (m\u00b3)", title_font_size=12, row=1, col=1
        )

        figure.update_yaxes(
            title_text="Total Pressure (Pa)", title_font_size=12, row=1, col=2
        )

        figure.update_layout(
            template="plotly_white",
            height=400,
            # autosize=True,  # Allow the figure to be autosized
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
                "text": "<b>Oil and Water Total Rate on Pressure Comparison</b>",
                "y": 0.95,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 24},
            },
        )

        return html.Div(
            dcc.Graph(figure=figure),
            id=ids.OIL_VS_WATER_SUBPLOTS,
            className=cns.PPD_OIL_VS_WATER_SUBPLOTS,
        )

    return html.Div(
        id=ids.OIL_VS_WATER_SUBPLOTS, className=cns.PPD_OIL_VS_WATER_SUBPLOTS
    )
