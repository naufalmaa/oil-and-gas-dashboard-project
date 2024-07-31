from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        [
            dmc.Header(  # separator provided
                height=40,
                # fixed=True,
                children=[
                    
                    dmc.Group([
                        
                        dmc.Anchor("Home", href="/", underline=False),
                        dmc.Text("     |     ", color="#e9ecef"),
                        dmc.Anchor("Projects", href="/", underline=False),
                        dmc.Text("     |     ", color="#e9ecef"),
                        dmc.Anchor("Dashboards", href="/", underline=False),
                        dmc.Text("     |     ", color="#e9ecef"),
                        dmc.Anchor("About", href="/", underline=False),
                        dmc.Text("     |     ", color="#e9ecef"),
                        dmc.TextInput(
                            style={"width": 250},
                            placeholder="Search...",
                            rightSection=DashIconify(icon="ic:round-search"),
                        ),
                        dmc.Text("     |     ", color="#e9ecef"),
                        DashIconify(
                            className=cns.OVW_SC_ICON,
                            # id=ids.ICON_TITLE_SUMMARY_TOGETHER,
                            icon="ic:baseline-account-box",
                            # color="#012226",
                            height=25,
                            width=25,
                            # style={
                                # "marginTop": 5,
                                # "marginRight": 10,
                                # "float": "left",
                            # },
                        ),
                        dmc.Anchor("Sign in", href="http://127.0.0.1:7654/", underline=False),
                        dmc.Text("     |     ", color="#e9ecef"),
                        # dmc.Image(
                        # src="/assets/waviv_logo.jpg",
                        # # alt="superman",
                        # # caption="Funny Meme",
                        # width=100,
                        # style={
                        #         "marginTop": 5,
                        #         # "marginRight": 10,
                        #         "float": "left",
                        #     },
                        # ),
                    ], 
                    className='header-center',
                    sx={'justifyContent': 'center'}
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
