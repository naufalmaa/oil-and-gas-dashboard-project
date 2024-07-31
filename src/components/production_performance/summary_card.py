from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD, "children"),
        Output(ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD, "children"),
        Output(ids.TOTAL_WATER_INJECTION_AMOUNT_CARD, "children"),
        Output(ids.ON_STREAM_TIME_AMOUNT_CARD, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER, "value"),
            Input(ids.TO_DATE_DATEPICKER, "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],
        prevent_initial_call=True,
    )
    def calculate_total(from_date: str, to_date: str, wells: list[str]) -> float:
        generate_sum_oil = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).sum_oil
        generate_sum_gas = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).sum_gas
        generate_sum_wi = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).sum_wi
        generate_sum_on_hours = source.filter(
            from_date=from_date, to_date=to_date, wells=wells
        ).sum_on_hours

        abb_sum_oil = source.abbreviate_value(generate_sum_oil)
        abb_sum_gas = source.abbreviate_value(generate_sum_gas)
        abb_sum_wi = source.abbreviate_value(generate_sum_wi)
        abb_sum_on_hours = source.abbreviate_value(generate_sum_on_hours)

        return (
            f"{abb_sum_oil}",
            f"{abb_sum_gas}",
            f"{abb_sum_wi}",
            f"{abb_sum_on_hours}",
        )

    return html.Div(
        html.Div(
            className=cns.PPD_SUMMARY_CARD_LEFT_GRID,
            children=[
                dmc.CardSection(
                    className=cns.PPD_SC_CARD_LEFT_GRID,
                    children=[
                        dmc.SimpleGrid(
                            className=cns.PPD_SC_SIMPLEGRID_LEFT_GRID,
                            cols=4,
                            children=[
                                dmc.Group(
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                DashIconify(
                                                    className=cns.PPD_SC_ICON_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="fa6-solid:gas-pump",
                                                    color="#CE6D7D",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Oil Production (m\u00b3)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 20,
                                                    },
                                                ),
                                                dmc.Text(
                                                    # "11.0M",
                                                    id=ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #151515",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                DashIconify(
                                                    className=cns.PPD_SC_ICON_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="mdi:gas",
                                                    color="#DDCC77",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 5,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Gas Production (m\u00b3)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight=500,
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='yellow',
                                                    style={"fontSize": 20},
                                                ),
                                                dmc.Text(
                                                    # "1,234.5M",
                                                    id=ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='yellow',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #151515",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                DashIconify(
                                                    className=cns.PPD_SC_ICON_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="fluent:water-32-filled",
                                                    color="#88CCEE",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 5,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Water Injection (m\u00b3)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight=500,
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='blue',
                                                    style={"fontSize": 20},
                                                ),
                                                dmc.Text(
                                                    # "54.3M",
                                                    id=ids.TOTAL_WATER_INJECTION_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='blue',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #151515",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                DashIconify(
                                                    className=cns.PPD_SC_ICON_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="mdi:timer-cog",
                                                    color="#012226",
                                                    height=40,
                                                    width=40,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 5,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total On Stream Time (Hours)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight=500,
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    style={"fontSize": 20},
                                                ),
                                                dmc.Text(
                                                    # "321K",
                                                    id=ids.ON_STREAM_TIME_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
                                                    align="center",
                                                    color="#25262B",
                                                    # color='black',
                                                    style={
                                                        "fontSize": 40,
                                                        "fontWeight": "bold",
                                                    },
                                                ),
                                            ],
                                            withBorder=True,
                                            radius="20px",
                                            style={
                                                "background-color": "#FFFFFF",
                                                "border": "2px solid #151515",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                            style={"marginTop": 20},
                        ),
                    ],
                )
            ],
        ),
        # style={'display': 'grid', 'grid-template-columns': '1fr 1fr 1fr 1fr', 'grid-template-rows': 'auto'},
        className=cns.PPD_SUMMARY_CARD_LEFT_GRID,
    )
