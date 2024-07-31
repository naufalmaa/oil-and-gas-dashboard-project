from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify

# from ...data.loader import ProductionDataSchema
from ...data.source import DataSource 

from .. import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.FROM_DATE_DATEPICKER_OVERVIEW, "value"),
        [
            Input(ids.ALL_DATES_BEFORE_CHECKBOX_OVERVIEW, "checked")
        ], prevent_initial_call=True
    )
    
    def select_earliest_date(checked: bool) -> str:
        if checked == True:
            return source.earliest_date
        if checked == False:
            pass
    
    return html.Div(
        className=cns.OVW_FROM_DATE_PICKER_WRAPPER,
        id = ids.FROM_DATEPICKER_LAYOUT_OVERVIEW,
        children=[
                        
            html.H5("From:", className=cns.PPD_H5),
            
            dmc.DatePicker(
                id=ids.FROM_DATE_DATEPICKER_OVERVIEW,
                className=cns.OVW_FROM_DATE_PICKER_DATEPICKER,
                value=source.earliest_date,
                dropdownPosition='flip',
                initialLevel='year',
                style={'marginTop':'5px', 'marginRight':'10px', "width": 175},
            ),

            dmc.Checkbox(
                id=ids.ALL_DATES_BEFORE_CHECKBOX_OVERVIEW,
                className=cns.OVW_ALL_DATE_PICKER_CHECKBOX,
                label='Earliest date',
                checked=True,
                value=source.earliest_date,
                color='dark',
                style={'marginTop':'10px'}
            ),
            
        ]
    )