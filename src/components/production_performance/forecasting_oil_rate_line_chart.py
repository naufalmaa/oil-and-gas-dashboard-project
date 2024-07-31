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
        Output(ids.FORECASTING_OIL_RATE_LINE_CHART, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER,  "value"),
            Input(ids.TO_DATE_DATEPICKER,    "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],  prevent_initial_call=True
    )
    
    def update_line_chart(from_date: str, to_date: str, wells: list[str]) -> html.Div:
        filtered_source_pt = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_date_well_ma(ProductionDataSchema.MOVING_AVERAGE_OIL)
#     #     if not filtered_source.row_count:
#     #         return html.Div(i18n.t("general.no_data"), id=ids.BAR_CHART)

        fig = px.line(
                filtered_source_pt,
                x=ProductionDataSchema.DATE,
                y=ProductionDataSchema.MOVING_AVERAGE_OIL,
                color=ProductionDataSchema.WELLBORE,
                labels={
                    "MOVING_AVERAGE_OIL":"14-days Moving Average Oil (m3)",
                    "DATEPRD": "Year",
                    "WELL_BORE_CODE": "Wells"
                },
                # style={}
            )

        return html.Div(dcc.Graph(figure=fig), id=ids.FORECASTING_OIL_RATE_LINE_CHART, className=cns.PPD_SECOND_CHART_LEFT_GRID)

    return html.Div(id=ids.FORECASTING_OIL_RATE_LINE_CHART, className=cns.PPD_SECOND_CHART_LEFT_GRID)
