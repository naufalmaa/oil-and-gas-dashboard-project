# import pandas as pd
from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

# from ...data.loader import ProductionDataSchema
from ...data.source import DataSource 

from .. import ids, cns

from ..production_performance.multiselect_helper import to_multiselect_options
    
def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.BLOCK_MULTISELECT_FILTER_OVERVIEW, "value"),
        [
            Input(ids.FROM_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.TO_DATE_DATEPICKER_OVERVIEW, "value"),
            Input(ids.SELECT_ALL_BLOCK_BUTTON_OVERVIEW, "n_clicks")
        ],
    )
    
    def select_all_blocks(from_date: str, to_date: str, _: int) -> list[str]:
        filter_unique_blocks = source.filter_overview(from_date=from_date, to_date=to_date).unique_blocks
        
        
        return filter_unique_blocks
        
    return html.Div(
        className=cns.OVW_MULTISELECT_WRAPPER,
        children=[
            html.H5("Blocks:", className=cns.PPD_H5),
            
            dmc.MultiSelect(
                id=ids.BLOCK_MULTISELECT_FILTER_OVERVIEW,
                className=cns.OVW_MULTISELECT_MULTISELECT,
                data=to_multiselect_options(source.unique_blocks),
                value=source.unique_blocks,
                placeholder="Select Blocks",
                searchable=True,
                clearable=True,
                nothingFound="No options available",
                style={'width':'98%','marginTop':'5px', 'paddingBottom':'20px'}
            ),
            dmc.Button(
                'Select All',
                id=ids.SELECT_ALL_BLOCK_BUTTON_OVERVIEW,
                className=cns.OVW_MULTISELECT_BUTTON,
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':'30px','marginBottom':'15px'},
                n_clicks=0,
            ),
        ]
    )