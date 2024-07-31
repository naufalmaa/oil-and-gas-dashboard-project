from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify

# from ...data.loader import ProductionDataSchema
from ...data.source import DataSource 

from .. import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.FROM_DATE_DATEPICKER, "value"),
        [
            Input(ids.ALL_DATES_BEFORE_CHECKBOX, "checked")
        ], prevent_initial_call=True
    )
    
    def select_earliest_date(checked: bool) -> str:
        if checked == True:
            return source.earliest_date
        if checked == False:
            pass
    
    # @app.callback(
    #     Output(ids.ALL_DATES_BEFORE_CHECKBOX, "checked"),
    #     Output(ids.ALL_DATES_AFTER_CHECKBOX, "checked"),
    #     Input(ids.ALL_DATES_MAIN_BUTTON, "n_clicks"),
    #     State(ids.ALL_DATES_BEFORE_CHECKBOX, "checked"),
    #     State(ids.ALL_DATES_AFTER_CHECKBOX, "checked")

    # )
    
    # def select_earliest_and_latest_date(n_clicks: int, checked1: bool, checked2: bool):
    #     if n_clicks:
    #         return True, True
    #     return checked1, checked2
    
    return html.Div(
        className=cns.PPD_FROM_DATE_PICKER_WRAPPER,
        id = ids.FROM_DATEPICKER_LAYOUT,
        children=[
                        
            html.H5("From:", className=cns.PPD_H5),
            
            dmc.DatePicker(
                id=ids.FROM_DATE_DATEPICKER,
                className=cns.PPD_FROM_DATE_PICKER_DATEPICKER,
                value=source.earliest_date,
                dropdownPosition='flip',
                initialLevel='year',
                style={'marginTop':'5px', 'marginRight':'10px', "width": 175},
            ),

            dmc.Checkbox(
                id=ids.ALL_DATES_BEFORE_CHECKBOX,
                className=cns.PPD_ALL_DATE_PICKER_CHECKBOX,
                label='Earliest date',
                checked=True,
                value=source.earliest_date,
                color='dark',
                style={'marginTop':'10px'}
            ),
            
            # dmc.Button(
            #     'Select All',
            #     id=ids.ALL_DATES_MAIN_BUTTON,
            #     className=cns.PPD_FROM_DATE_PICKER_BUTTON,
            #     variant="outline",
            #     color="dark",
            #     radius="5px",
            #     leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
            #     style={'height':30, 'marginTop':'10px'},
            #     n_clicks=0,
            # ),
            
        ]
    )