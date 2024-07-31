# import pandas as pd
from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

# from ...data.loader import ProductionDataSchema
from ...data.source import DataSource 

from .. import ids, cns

from .multiselect_helper import to_multiselect_options
    
def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.WELL_MAIN_MULTISELECT, "value"),
        [
            Input(ids.FROM_DATE_DATEPICKER, "value"),
            Input(ids.TO_DATE_DATEPICKER, "value"),
            Input(ids.SELECT_ALL_WELLS_MAIN_BUTTON, "n_clicks")
        ],
    )
    
    def select_all_wells(from_date: str, to_date: str, _: int) -> list[str]:
        return source.filter(from_date=from_date, to_date=to_date).unique_wells
        
    return html.Div(
        className=cns.PPD_MULTISELECT_WRAPPER,
        children=[
            html.H5("Well:", className=cns.PPD_H5),
            
            dmc.MultiSelect(
                id=ids.WELL_MAIN_MULTISELECT,
                className=cns.PPD_MULTISELECT_MULTISELECT,
                data=to_multiselect_options(source.unique_wells),
                value=source.unique_wells,
                placeholder="Select Wells",
                searchable=True,
                clearable=True,
                nothingFound="No options available",
                style={'width':'98%','marginTop':'5px', 'paddingBottom':'20px'}
            ),
            dmc.Button(
                'Select All',
                id=ids.SELECT_ALL_WELLS_MAIN_BUTTON,
                className=cns.PPD_MULTISELECT_BUTTON,
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':'30px','marginBottom':'15px'},
                n_clicks=0,
            ),
        ]
    )