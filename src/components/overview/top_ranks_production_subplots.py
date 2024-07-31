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
        Output(ids.TOP_RANKS_OIL_GAS_SUBPLOTS, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.TO_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.BLOCK_MULTISELECT_FILTER_OVERVIEW, "value"),
        ],
        prevent_initial_call=True,
    )
    def update_subplots(from_date: str, to_date: str, blocks: list[str]) -> html.Div:
        if not blocks:
            empty_fig = make_subplots(rows=1, cols=1)
            empty_fig.update_layout(
                height=300,
                margin=dict(l=10, r=10, t=10, b=10),
            )
            return html.Div(
                dcc.Graph(figure=empty_fig),
                id=ids.TOP_RANKS_OIL_GAS_SUBPLOTS,
                className=cns.OVW_TOP_RANKS_OIL_GAS_SUBPLOTS,
            )

        # for productions
        filtered_source_production = source.filter_overview(
            from_date=from_date, to_date=to_date, blocks=blocks
        ).df_production

        result_df = source.create_table_prod_mth(
            df=filtered_source_production,
            type="avg_well"
        )
        
        # for formatting value only
        def format_value(value):
            if value >= 1e12:
                return f"{value / 1e12:.2f}T"
            elif value >= 1e9:
                return f"{value / 1e9:.2f}B"
            elif value >= 1e6:
                return f"{value / 1e6:.2f}M"
            elif value >= 1e3:
                return f"{value / 1e3:.2f}K"
            
            return str(value)

        # Initialize figure with subplots
        figure_ranks = make_subplots(
            rows=1,
            cols=2,
            # column_widths=[0.5, 0.5],
            subplot_titles=(
                "<b>Top Ranks of Oil Production/Month</b>",
                "<b>Top Ranks of Gas Production/Month</b>",
            ),
            # row_heights=[0.5, 0.5],
            specs=[
                [{"type": "bar"}, {"type": "bar"}],
            ],
            horizontal_spacing=0.2
        )

        # Bar chart for BORE_GAS_VOL
        figure_ranks.add_trace(
            go.Bar(
                name="Top Ranks of Oil Production/Month",
                y=result_df[ProductionDataSchema.WELLBORE],
                x=result_df['BORE_OIL_VOL_barrels'],
                orientation="h",
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                # fillpattern={'fillmode':'overlay', 'fgcolor':'rgb(3,166,166, 0.0001)'},
                marker=dict(
                        color='#CE6D7D',
                        ),
                showlegend=True,
                text=result_df['BORE_OIL_VOL_barrels'].apply(format_value),  # Display values on the bars
                textposition='auto'
            ),
            row=1,
            col=1,
        )

        # Bar chart for BORE_GAS_VOL
        figure_ranks.add_trace(
            go.Bar(
                name="Top Ranks of Gas Production/Month",
                y=result_df[ProductionDataSchema.WELLBORE],
                x=result_df['BORE_GAS_VOL_MCF'],
                orientation="h",
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                # fillpattern={'fillmode':'overlay', 'fgcolor':'rgb(3,166,166, 0.0001)'},
                marker=dict(
                        color='#DDCC77',
                        ),
                showlegend=True,
                text=result_df['BORE_GAS_VOL_MCF'].apply(format_value),  # Display values on the bars
                textposition='auto'
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
        figure_ranks.update_yaxes(
            title_text="Oil Volume (in Barrels)", title_font_size=12, row=1, col=1
        )

        figure_ranks.update_yaxes(
            title_text="Gas Volume (in MCF)", title_font_size=12, row=1, col=2
        )

        # # Set y-axis titles
        # figure_ranks.update_xaxes(
        #     range=[0, 350000], row=1, col=1
        # )

        # figure_ranks.update_xaxes(
        #     range=[0, 300000000000], row=1, col=2
        # )

        figure_ranks.update_layout(
            template="plotly_white",
            height=400,
            # autosize=True,  # Allow the figure to be autosized
            margin=dict(l=50, r=50, b=10),  # Adjust the margins for the figure
            legend=dict(
                x=0.45,  # Set the x position of the legend (0.5 means centered horizontally)
                y=1.2,  # Set the y position of the legend (1.0 means at the top)
                xanchor="center",  # Anchor point for the x position ('center' for center alignment)
                yanchor="top",  # Anchor point for the y position ('top' for top alignment)
                orientation="h",  # Orientation of the legend ('h' for horizontal)
                bgcolor="rgba(255, 255, 255, 0.5)",  # Background color of the legend (with transparency)
                # bordercolor='rgba(0, 0, 0, 0.5)',     # Border color of the legend (with transparency)
                # borderwidth=1       # Border width of the legend
            ),
            title={
                "text": "<b>Top Ranks of Production/Month</b>",
                "y": 0.95,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 24},
            },
        )

        return html.Div(
            dcc.Graph(figure=figure_ranks),
            id=ids.TOP_RANKS_OIL_GAS_SUBPLOTS,
            className=cns.OVW_TOP_RANKS_OIL_GAS_SUBPLOTS,
        )

    return html.Div(
        id=ids.TOP_RANKS_OIL_GAS_SUBPLOTS, className=cns.OVW_TOP_RANKS_OIL_GAS_SUBPLOTS
    )
