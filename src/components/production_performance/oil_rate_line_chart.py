from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

import pandas as pd

# import plotly.graph_objects as go
import plotly.express as px

from ...data.loader import ProductionDataSchema
from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.OIL_RATE_LINE_CHART, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER, "value"),
            Input(ids.TO_DATE_DATEPICKER, "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],
        prevent_initial_call=True,
    )
    def update_line_chart(from_date: str, to_date: str, wells: list[str]) -> html.Div:
        if not wells:  # Check if the 'wells' list is empty
            # If there are no wells selected, return an empty plot
            empty_fig = px.line(
                labels={
                    "MOVING_AVERAGE_OIL": "14-days Moving Average Oil (m3)",
                    "DATEPRD": "Year",
                    "WELL_BORE_CODE": "Wells",
                }
            )
            return html.Div(
                dcc.Graph(figure=empty_fig),
                id=ids.OIL_RATE_LINE_CHART,
                className=cns.PPD_OIL_RATE_LINE_CHART,
            )

        filtered_source_pt = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).create_pivot_table_date_well_ma(ProductionDataSchema.MOVING_AVERAGE_OIL)
        #     #     if not filtered_source.row_count:
        #     #         return html.Div(i18n.t("general.no_data"), id=ids.BAR_CHART)

        fig = px.line(
            filtered_source_pt,
            x=ProductionDataSchema.DATE,
            y=ProductionDataSchema.MOVING_AVERAGE_OIL,
            color=ProductionDataSchema.WELLBORE,
            color_discrete_sequence=px.colors.qualitative.Safe,
            labels={
                "MOVING_AVERAGE_OIL": "14-days Moving Average Oil (m3)",
                "DATEPRD": "Year",
                "WELL_BORE_CODE": "Wells",
            }
            # style={}
        )

        fig.update_layout(
            template="plotly_white",
            title={
                "text": "<b>Oil Production Rate</b>",
                "y": 0.95,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
                "font": {"size": 24},
            },
        )

        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.OIL_RATE_LINE_CHART,
            className=cns.PPD_OIL_RATE_LINE_CHART,
        )

    return html.Div(id=ids.OIL_RATE_LINE_CHART, className=cns.PPD_OIL_RATE_LINE_CHART)
