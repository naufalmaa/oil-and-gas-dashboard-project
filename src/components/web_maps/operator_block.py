from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns
from ..production_performance.multiselect_helper import to_multiselect_options


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.BLOCK_NAME_MULTISELECT, "value"),
        [
            Input(ids.OPERATOR_BLOCK_MULTISELECT, "value")
        ],
    )
    
    def operator_block(chosen_operator_block: str) -> list[str]:
        operator_block_df = source.filter_block(operator_block=chosen_operator_block).to_dataframe_geopandas_temp
        return operator_block_df['operator']
    
    return html.Div(
        children=[
            html.H5('Operator'),
            dmc.MultiSelect(
                id=ids.OPERATOR_BLOCK_MULTISELECT,
                placeholder='Select Operator Name',
                data=to_multiselect_options(source.all_operator_block).unique(),
                value=source.all_operator_block.unique(),
                searchable=True,
                clearable=True,
                nothingFound="No options available",
                style={'width':450,'marginTop':'5px'}
            )
        ]
    )