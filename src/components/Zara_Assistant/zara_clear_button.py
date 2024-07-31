from dash import Dash, html, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ...data.source import DataSource
from ...components import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.RESPONSE_CHAT, 'children', allow_duplicate=True),
        Input(ids.CLEAR_CONVO, 'n_clicks'),
    )
    def clear_convo(clicked):
        global conv_hist
        if clicked:
            convo_hist.clear()
            return convo_hist
        else:
            pass

    return html.Div(
        dmc.Button('Clear', id=ids.CLEAR_CONVO, variant='outline', leftIcon=DashIconify(icon='mdi:trash-outline'))
    )
