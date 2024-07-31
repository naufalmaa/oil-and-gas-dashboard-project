from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns
from ..production_performance.multiselect_helper import to_multiselect_options

import json


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.BLOCK_NAME_MULTISELECT, "value"), 
        [
            Input(ids.STATUS_BLOCK_CHECKBOX, "value"),
            Input(ids.OPERATOR_BLOCK_MULTISELECT, "value"),
            Input(ids.NUMBER_OF_WELL_SLIDER, "value"),
            Input(ids.SHAPE_AREA_SLIDER, "value"),
            Input(ids.RESERVE_SLIDER, "value"),
        ],
    )
    def filter_block_func(
        chosen_status_block: str,
        chosen_operator_block: str,
        chosen_total_well: int,
        chosen_shape_area: float,
        chosen_reserve: float,
    ) -> list[str]:
        df_filtered_input = source.filter_block(
            status_block=chosen_status_block,
            operator_block=chosen_operator_block,
            total_wellMin=chosen_total_well[0],
            total_wellMax=chosen_total_well[1],
            sq_kmMin=chosen_shape_area[0],
            sq_kmMax=chosen_shape_area[1],
            reserveMin=chosen_reserve[0],
            reserveMax=chosen_reserve[1],
        ).to_dataframe_geopandas_temp
        return df_filtered_input["name"]

    return html.Div(
        children=[
            html.H5("Block"),
            dmc.MultiSelect(
                id=ids.BLOCK_NAME_MULTISELECT,
                data=to_multiselect_options(source.all_name_blocks),
                value=source.all_name_blocks,
                placeholder="Select Blocks",
                searchable=True,
                clearable=True,
                nothingFound="No options available",
                style={"width": "98%", "marginTop": "5px", "paddingBottom": "20px"},
            ),
            html.H5("Status"),
            dmc.CheckboxGroup(
                id=ids.STATUS_BLOCK_CHECKBOX,
                orientation="vertical",
                children=[
                    dmc.Checkbox(
                        label="Exploration",
                        value="Exploration",
                        color="dark",
                        style={"marginTop": 0},
                    ),
                    dmc.Checkbox(
                        label="Development",
                        value="Development",
                        color="dark",
                        style={"marginTop": -15},
                    ),
                    dmc.Checkbox(
                        label="Production",
                        value="Production",
                        color="dark",
                        style={"marginTop": -15},
                    ),
                    # dmc.Checkbox(
                    #     label="Abandoned",
                    #     value="Abandoned",
                    #     color="dark",
                    #     style={"marginTop": -15},
                    # ),
                ],
                value=source.unique_status,
                style={"width": "98%", "paddingBottom": "20px"},
            ),
            html.H5("Operator"),
            dmc.MultiSelect(
                id=ids.OPERATOR_BLOCK_MULTISELECT,
                placeholder="Select Operator Name",
                data=to_multiselect_options(source.unique_operator),
                value=source.unique_operator,
                searchable=True,
                clearable=True,
                nothingFound="No options available",
                style={"width": "98%", "paddingBottom": "20px"},
            ),
            html.H5("Number of Wells"),
            dmc.RangeSlider(
                id=ids.NUMBER_OF_WELL_SLIDER,
                value=[source.minimum_total_well, source.maximum_total_well],
                max=60,
                min=0,
                marks=[
                    {"value": 10, "label": "10"},
                    {"value": 30, "label": "30"},
                    {"value": 50, "label": "50"},
                ],
                style={"width": "98%", "marginTop": 10, "marginBottom": 30},
                color="dark",
            ),
            html.H5("Shape Area in Sq. Kilometes"),
            dmc.RangeSlider(
                id=ids.SHAPE_AREA_SLIDER,
                value=[source.minimum_area_km, source.maximum_area_km],
                max=350,
                min=0,
                marks=[
                    {"value": 50, "label": "50"},
                    {"value": 150, "label": "150"},
                    {"value": 250, "label": "250"},
                ],
                style={"width": "98%", "marginTop": 10, "marginBottom": 30},
                color="dark",
            ),
            html.H5("Estimated Reserve in Millions of Barrels Oil"),
            dmc.RangeSlider(
                id=ids.RESERVE_SLIDER,
                value=[source.minimum_reserve, source.maximum_reserve],
                max=600,
                min=0,
                marks=[
                    {"value": 100, "label": "100"},
                    {"value": 300, "label": "300"},
                    {"value": 500, "label": "500"},
                ],
                style={"width": "98%", "marginTop": 10, "marginBottom": 30},
                color="dark",
            ),
        ]
    )
