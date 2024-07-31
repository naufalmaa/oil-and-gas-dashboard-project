from dash import Dash, html, Input, Output, callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ...data.source import DataSource
from ...components import ids, cns

from ..Zara_Assistant import Zara_Chatbot_v2, zara_tab, preview_data, zara_clear_button


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.ZARA_DRAWER, "opened"),
        Input(ids.ZARA_FLOAT_BUTTON, "n_clicks"),
        prevent_initial_call=True,
    )
    def drawer_zara(n_clicks):
        return True

    return html.Div(
        children=[
            dmc.Button(
                "Ask Zara",
                className=cns.ZARA_FLOAT_BUTTON,
                id=ids.ZARA_FLOAT_BUTTON,
                variant="gradient",
                gradient={"from": "indigo", "to": "cyan"},
                leftIcon=DashIconify(icon="material-symbols:face-3", width=20),
            ),
            dmc.Drawer(
                id=ids.ZARA_DRAWER,
                lockScroll=False,
                overlayOpacity=0.2,
                size="70%",
                zIndex=1000,
                children=[
                    html.Div(
                        className="parent-card",
                        children=[
                            dmc.Card(
                                className=cns.ZARA_CARD_SECTION,
                                withBorder=True,
                                shadow="0px",
                                radius="lg",
                                children=[
                                    dmc.LoadingOverlay(
                                        html.Div(
                                            className=cns.ZARA_RESPONSE_SECTION,
                                            id=ids.RESPONSE_CHAT,
                                        ),
                                    )
                                ],
                            ),
                            dmc.Card(
                                className=cns.ZARA_CARD_INTRO,
                                withBorder=True,
                                shadow="0px",
                                radius="lg",
                                children=[
                                    html.Div(
                                        children=[
                                            dmc.Text(
                                                "Welcome to Zara!",
                                                style={
                                                    "fontWeight": "600",
                                                    "fontSize": "30px",
                                                },
                                            ),
                                            dmc.Text(
                                                "An assistant for you to build a quick data analysis without querying your data"
                                            ),
                                            html.Div(zara_tab.render(app, source)),
                                            # html.Div(zara_clear_button.render(app, source))
                                        ]
                                    )
                                ],
                            ),
                            dmc.Card(
                                className=cns.ZARA_CARD_TABLE,
                                withBorder=True,
                                shadow="0px",
                                radius="lg",
                                children=[preview_data.render(app, source)],
                            ),
                        ],
                    ),
                    Zara_Chatbot_v2.render(app, source),
                ],
            ),
        ]
    )
