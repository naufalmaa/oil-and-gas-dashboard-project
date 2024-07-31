from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.TOTAL_OIL_BLOCKS_AMOUNT_CARD, "children"),
        Output(ids.TOTAL_OPERATORS_AMOUNT_CARD, "children"),
        Output(ids.TOTAL_NUM_OF_WELLS_AMOUNT_CARD, "children"),
        Output(ids.AVG_OIL_PRODUCTION_MONTH_AMOUNT_CARD, "children"),
        Output(ids.AVG_GAS_PRODUCTION_MONTH_AMOUNT_CARD, "children"),
        Output(ids.AVG_DEPTH_AMOUNT_CARD, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.TO_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.BLOCK_MULTISELECT_FILTER_OVERVIEW, "value"),
        ],
        prevent_initial_call=True,
    )
    def calculate_total(from_date: str, to_date: str, blocks: list[str]) -> float:
        generate_name_oil_blocks = source.filter_overview(from_date=from_date, to_date=to_date, blocks=blocks).unique_blocks
        
        generate_amount_oil_blocks = source.filter_overview(from_date=from_date, to_date=to_date, blocks=blocks).amount_blocks
        
        generate_amount_operators = source.generator_amount(generate_name_oil_blocks, "amount_operator")
        generate_num_wells = source.generator_amount(generate_name_oil_blocks, "num_wells")
        generate_avg_oil_prod_block = source.generator_amount(generate_name_oil_blocks, "avg_oil_prod_block")
        generate_avg_gas_prod_block = source.generator_amount(generate_name_oil_blocks, "avg_gas_prod_block")
        generate_avg_depth = source.generator_amount(generate_name_oil_blocks, "avg_depth")
        
        
        abb_amount_blocks = source.abbreviate_value(generate_amount_oil_blocks)
        abb_amount_operators = source.abbreviate_value(generate_amount_operators)
        abb_num_wells = generate_num_wells
        abb_avg_oil_prod_block = source.abbreviate_value(generate_avg_oil_prod_block)
        abb_avg_gas_prod_block = source.abbreviate_value(generate_avg_gas_prod_block)
        abb_avg_depth = generate_avg_depth
        
        
        return (
            f"{abb_amount_blocks}",
            f"{abb_amount_operators}",
            f"{abb_num_wells}",
            f"{abb_avg_oil_prod_block}",
            f"{abb_avg_gas_prod_block}",
            f"{abb_avg_depth:,.2f}"
        )

    return html.Div(
        html.Div(
            className=cns.OVW_SUMMARY_CARD_WRAPPER,
            children=[
                dmc.CardSection(
                    className=cns.OVW_SC_CARDSECTION,
                    children=[
                        dmc.SimpleGrid(
                            className=cns.OVW_SC_SIMPLEGRID,
                            cols=6,
                            children=[
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="material-symbols:factory",
                                                    color="#012226",
                                                    height=30,
                                                    width=30,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Oil Blocks",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 18,
                                                    },
                                                ),
                                                dmc.Text(
                                                    # "5",
                                                    id=ids.TOTAL_OIL_BLOCKS_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
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
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="mdi:worker",
                                                    color="#012226",
                                                    height=30,
                                                    width=30,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Operators",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 17,
                                                    },
                                                ),
                                                dmc.Text(
                                                    # "5",
                                                    id=ids.TOTAL_OPERATORS_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
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
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="fa6-solid:oil-well",
                                                    color="#012226",
                                                    height=30,
                                                    width=30,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Total Number of Wells / Monitor Wells",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 13,
                                                    },
                                                ),
                                                dmc.Text(
                                                    # "120 - 9",
                                                    id=ids.TOTAL_NUM_OF_WELLS_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
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
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="material-symbols:oil-barrel",
                                                    color="#012226",
                                                    height=30,
                                                    width=30,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Average Oil Production (m\u00b3)",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 15,
                                                    },
                                                ),
                                                dmc.Text(
                                                    # "22K",
                                                    id=ids.AVG_OIL_PRODUCTION_MONTH_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
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
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="ic:sharp-gas-meter",
                                                    color="#012226",
                                                    height=30,
                                                    width=30,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Average Gas Production (m\u00b3)",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 15,
                                                    },
                                                ),
                                                dmc.Text(
                                                    # "300K",
                                                    id=ids.AVG_GAS_PRODUCTION_MONTH_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
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
                                                "border": "2px solid #012226",
                                            },
                                        ),
                                    ],
                                ),
                                dmc.Group(
                                    className=cns.OVW_SC_GROUP,
                                    children=[
                                        dmc.Card(
                                            className=cns.OVW_SC_CARD,
                                            children=[
                                                DashIconify(
                                                    className=cns.OVW_SC_ICON,
                                                    # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                                                    icon="iconoir:depth",
                                                    color="#012226",
                                                    height=30,
                                                    width=30,
                                                    style={
                                                        "marginTop": 5,
                                                        "marginRight": 10,
                                                        "float": "left",
                                                    },
                                                ),
                                                dmc.Title(
                                                    f"Average Depth of Wells (TVD) (m)",
                                                    className=cns.OVW_SC_TITLE,
                                                    # id=ids.AVG_DEPTH_AMOUNT_CARD,
                                                    weight="500",
                                                    order=5,
                                                    align="left",
                                                    color="#25262B",
                                                    # color='red',
                                                    style={
                                                        "marginLeft": 10,
                                                        "fontSize": 15,
                                                    },
                                                ),
                                                dmc.Text(
                                                    # "5.2K",
                                                    id=ids.AVG_DEPTH_AMOUNT_CARD,
                                                    className=cns.OVW_SC_TEXT,
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
                                                "border": "2px solid #012226",
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
        className=cns.OVW_SUMMARY_CARD_WRAPPER,
    )
