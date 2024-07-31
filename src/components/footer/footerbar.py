from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        [
            dmc.Footer(  # separator provided
                height=30,
                # fixed=True,
                children=[
                    
                    dmc.Group([
                        
                        dmc.Anchor("© 2023 Waviv Technologies Company. All rights reserved.", href="/", underline=False,
                                   style={
                                        "fontSize": 12,
                                        "fontWeight": "regular",
                                        "color": "#c1c1c1",
                                    },),
                        dmc.Text("     |     ", color="#e9ecef"),
                        dmc.Anchor("Privacy Notice", href="/", underline=False, color="#e9ecef",
                                   style={
                                        "fontSize": 12,
                                        "fontWeight": "regular",
                                        "color": "#c1c1c1",
                                    },),
                        dmc.Text("     |     ", color="#e9ecef"),
                        dmc.Anchor("Terms of Use", href="/", underline=False, color="#e9ecef",
                                   style={
                                        "fontSize": 12,
                                        "fontWeight": "regular",
                                        "color": "#c1c1c1",
                                    },),
                        dmc.Text("     |     ", color="#e9ecef"),
                        
                        
                    ], 
                    className='footer-right',
                    sx={'justifyContent': 'right'}
                    ),
                    # dmc.Anchor("Home", href="/", underline=False),
                    # dmc.Anchor("Projects", href="/", underline=False),
                    # dmc.Anchor("Dashboards", href="/", underline=False),
                    # dmc.Anchor("More", href="/", underline=False),
                    # dmc.Breadcrumbs(
                    #     # separator="→",
                    #     separator=" || ",
                    #     children=[
                    #         dmc.Anchor("Home", href="/", underline=False),
                    #         dmc.Anchor("Projects", href="/", underline=False),
                    #         dmc.Anchor("Dashboards", href="/", underline=False),
                    #         dmc.Anchor("More", href="/", underline=False),
                    #     ],
                    # ),
                    dmc.Space(h=50),
                ],
            )
        ]
    )
