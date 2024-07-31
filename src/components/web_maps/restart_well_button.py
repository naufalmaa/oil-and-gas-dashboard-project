from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from ...components import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:

    @app.callback(
        Output(ids.WELL_NAME_MULTISELECT,'value'),
        Output(ids.ORIENTATION_WELL_CHECKBOX,'value'),
        Output(ids.STATUS_WELL_CHECKBOX,'value'),
        Output(ids.PURPOSE_WELL_CHECKBOX,'value'),
        Output(ids.TYPE_WELL_CHECKBOX,'value'),
        [
            Input(ids.RESTART_FILTER_WELL_MAP,'n_clicks')
        ],
        prevent_initial_call=True,
    )

    def reset_filter_well(n_clicks):
        if n_clicks is None:
            raise PreventUpdate
        else:
            # reset_df = all_wells[(all_wells['orient'].isin(all_wells['orient'])) & (all_wells['status'].isin(all_wells['status'])) & (all_wells['purpose'].isin(all_wells['purpose'])) & (all_wells['type'].isin(all_wells['type']))]
            # all_orientation_well
            # all_status_well
            # all_purpose_well
            # all_type_well
            reset_well_name = source.all_name_well
            reset_orient = source.all_orientation_well
            reset_status = source.all_status_well
            reset_purpose = source.all_purpose_well
            reset_type = source.all_type_well
            
            return reset_well_name, reset_orient, reset_status, reset_purpose, reset_type
        
    return html.Div(
        children=[
            dmc.Button(
                'Reset',
                id=ids.RESTART_FILTER_WELL_MAP,
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