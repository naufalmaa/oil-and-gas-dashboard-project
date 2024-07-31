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
        Output(ids.WELL_STATS_SUBPLOTS, "children"),
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
            empty_fig.update_layout(height=800)
            return html.Div(
                dcc.Graph(figure=empty_fig),
                id=ids.WELL_STATS_SUBPLOTS,
                className=cns.PPD_WELL_STATS_SUBPLOTS,
            )

        filtered_pt_cum_oil_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date(ProductionDataSchema.BORE_OIL_VOL)
        filtered_pt_cum_oil_well = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_well(ProductionDataSchema.BORE_OIL_VOL)

        filtered_pt_cum_gas_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date(ProductionDataSchema.BORE_GAS_VOL)
        filtered_pt_cum_gas_well = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_well(ProductionDataSchema.BORE_GAS_VOL)

        filtered_pt_cum_water_date = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date(
            ProductionDataSchema.BORE_WAT_VOL, ProductionDataSchema.BORE_WI_VOL
        )
        filtered_pt_cum_water_well = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_well(
            ProductionDataSchema.BORE_WAT_VOL, ProductionDataSchema.BORE_WI_VOL
        )

        colors = [
            "#88CCEE",
            "#DDCC77",
            "#CC6677",
            "#117733",
            "#332288",
            "#AA4499",
            "#44AA99",
            "#999933",
            "#882255",
            "#661100",
            "#888888",
        ]

        # Initialize figure with subplots
        figure = make_subplots(
            rows=3,
            cols=2,
            column_widths=[0.7, 0.3],
            row_heights=[0.4, 0.4, 0.4],
            specs=[
                [{"type": "scatter"}, {"type": "pie"}],
                [{"type": "scatter"}, {"type": "pie"}],
                [{"type": "scatter"}, {"type": "pie"}],
            ],
        )
        # Oil line chart and pie
        # Add Line
        figure.add_trace(
            go.Scatter(
                name="Total Oil Vol by Time (m\u00b3)",
                x=filtered_pt_cum_oil_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_oil_date[ProductionDataSchema.BORE_OIL_VOL],
                mode="lines",
                fill="tozeroy",
                line={"color": "#CC6677"},
                showlegend=True,
                legendrank=1,
            ),
            row=1,
            col=1,
        )

        # Add Pie
        figure.add_trace(
            go.Pie(
                name="Total Oil Vol by Well (m\u00b3)",
                title_text="<b>Total Oil Vol by Well (m\u00b3)</b><br>&nbsp;",
                title_position="top center",
                title_font_size=12,
                # text=filtered_pt_cum_oil_well[ProductionDataSchema.WELLBORE].to_list(),
                # textposition="inside",
                labels=filtered_pt_cum_oil_well[
                    ProductionDataSchema.WELLBORE
                ].to_list(),
                values=filtered_pt_cum_oil_well[
                    ProductionDataSchema.BORE_OIL_VOL
                ].to_list(),
                hole=0.5,
            ),
            row=1,
            col=2,
        )

        # pt_cum_gas_well
        # pt_cum_gas_date

        # Gas line chart and pie
        # Add Line
        figure.add_trace(
            go.Scatter(
                name="Total Gas Vol by Time (m\u00b3)",
                x=filtered_pt_cum_gas_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_gas_date[ProductionDataSchema.BORE_GAS_VOL],
                mode="lines",
                fill="tozeroy",  # Set fill to 'tozeroy' for area below the line
                line={"color": "#E3D691"},
                showlegend=True,
                legendrank=2,
            ),
            row=2,
            col=1,
        )

        # Add Pie
        figure.add_trace(
            go.Pie(
                name="Total Gas Vol by Well (m\u00b3)",
                title_text="<b>Total Gas Vol by Well (m\u00b3)</b><br>&nbsp;",
                title_position="top center",
                title_font_size=12,
                # text=filtered_pt_cum_gas_well[ProductionDataSchema.WELLBORE].to_list(),
                # textposition="inside",
                labels=filtered_pt_cum_gas_well[
                    ProductionDataSchema.WELLBORE
                ].to_list(),
                values=filtered_pt_cum_gas_well[
                    ProductionDataSchema.BORE_GAS_VOL
                ].to_list(),
                hole=0.5,
                marker=dict(colors=colors),
            ),
            row=2,
            col=2,
        )

        # pt_cum_water_well
        # pt_cum_water_date

        # Water line chart and pie
        # Add Line
        figure.add_trace(
            go.Scatter(
                name="Total Water Vol by Time (m\u00b3)",
                x=filtered_pt_cum_water_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_water_date[ProductionDataSchema.BORE_WAT_VOL],
                mode="lines",
                fill="tozeroy",  # Set fill to 'tozeroy' for area below the line
                line={"color": "#88CCEE"},
                showlegend=True,
                legendrank=3,
            ),
            row=3,
            col=1,
        )

        figure.add_trace(
            go.Scatter(
                name="Total Water Injection Vol by Time (m\u00b3)",
                x=filtered_pt_cum_water_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_water_date[ProductionDataSchema.BORE_WI_VOL],
                mode="lines",
                fill="tozeroy",  # Set fill to 'tozeroy' for area below the line
                fillpattern={
                    "fillmode": "overlay",
                    "fgcolor": "rgb(3,166,166, 0.0001)",
                },
                line={"color": "#6659A5", "width": 0.1},
                opacity=0.1,
                showlegend=True,
                legendrank=4,
            ),
            row=3,
            col=1,
        )

        # Add Pie
        figure.add_trace(
            go.Pie(
                name="Total Water Vol by Well (m\u00b3)",
                title_text="<b>Total Water Vol by Well (m\u00b3)</b><br>&nbsp;",
                title_position="top center",
                title_font_size=12,
                # text=filtered_pt_cum_water_well[ProductionDataSchema.WELLBORE].to_list(),
                # textposition="inside",
                labels=filtered_pt_cum_water_well[
                    ProductionDataSchema.WELLBORE
                ].to_list(),
                values=filtered_pt_cum_water_well[
                    ProductionDataSchema.BORE_WAT_VOL
                ].to_list(),
                hole=0.5,
                marker=dict(colors=colors),
                showlegend=False,
            ),
            row=3,
            col=2,
        )

        figure.update_yaxes(
            title_text="Oil Volume (m\u00b3)", title_font_size=12, row=1, col=1
        )
        figure.update_yaxes(
            title_text="Gas Volume (m\u00b3)", title_font_size=12, row=2, col=1
        )
        figure.update_yaxes(
            title_text="Water & Water Injection Vol (m\u00b3)",
            title_font_size=12,
            row=3,
            col=1,
        )

        figure.update_layout(
            height=800,
            autosize=True,  # Allow the figure to be autosized
            margin=dict(l=10, r=10, b=10),  # Adjust the margins for the figure
            legend=dict(
                x=1.2,  # Set the x position of the legend (0.5 means centered horizontally)
                y=1.0,  # Set the y position of the legend (1.0 means at the top)
                xanchor="center",  # Anchor point for the x position ('center' for center alignment)
                yanchor="top",  # Anchor point for the y position ('top' for top alignment)
                orientation="v",  # Orientation of the legend ('h' for horizontal)
                bgcolor="rgba(255, 255, 255, 0.5)",  # Background color of the legend (with transparency)
                # bordercolor='rgba(0, 0, 0, 0.5)',     # Border color of the legend (with transparency)
                # borderwidth=1       # Border width of the legend
            ),
            template="plotly_white",
            title={
                "text": "<b>Well Stats</b>",
                "y": 0.95,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 24},
            },
        )

        return html.Div(
            dcc.Graph(figure=figure),
            id=ids.WELL_STATS_SUBPLOTS,
            className=cns.PPD_WELL_STATS_SUBPLOTS,
        )

    return html.Div(
        id=ids.WELL_STATS_SUBPLOTS, className=cns.PPD_WELL_STATS_SUBPLOTS
    )
