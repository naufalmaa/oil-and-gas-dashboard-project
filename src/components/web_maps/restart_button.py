from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from ...components import ids, cns



def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.STATUS_BLOCK_CHECKBOX, 'value'),
        Output(ids.OPERATOR_BLOCK_MULTISELECT, 'value'),
        Output(ids.NUMBER_OF_WELL_SLIDER, 'value'),
        Output(ids.SHAPE_AREA_SLIDER, 'value'),
        Output(ids.RESERVE_SLIDER, 'value'),
        [
            Input(ids.RESTART_FILTER_MAP, "n_clicks")
        ],
        prevent_initial_call=True,
    )
    
    def restart_map(restart_filter: int) -> list[str]:
        if restart_filter is None:
            raise PreventUpdate
        else:
            restart_status = source.all_status_block
            restart_operator = source.unique_operator
            restart_well_slider = [source.minimum_total_well, source.maximum_total_well]
            restart_shape_area_slider = [source.minimum_area_km, source.maximum_area_km]
            restart_reserve_slider = [source.minimum_reserve, source.maximum_reserve]
            
            return restart_status, restart_operator, restart_well_slider, restart_shape_area_slider, restart_reserve_slider
            
    return html.Div(
        children=[
            dmc.Button(
                'Reset',
                id=ids.RESTART_FILTER_MAP,
                className="",
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':'30px','marginTop':'20px','marginBottom':'10px'},
                n_clicks=0,
            ),
            
        ]
    )