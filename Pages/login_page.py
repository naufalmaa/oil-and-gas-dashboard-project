# import dash
from dash import Dash, html, dcc, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    external_stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
    ],
)


app.layout = dmc.Center(
    style={
        "position": "absolute",
        "top": "50%",
        "left": "50%",
        "transform": "translate(-50%, -50%)",
    },
    children=[
        dmc.Card(
            children=[
                dmc.CardSection(
                    [
                        dmc.Title("Welcome to", order=4, align="center"),
                        # html.Br(),
                        dmc.Title("Dashboard Project!", order=2, align="center"),
                            dmc.Text(
                                "login with:",
                                # variant="dashed",
                                # labelPosition="center",
                                size="sm",
                                align="center",
                                mt="0.5rem",
                                mb="0.5rem",
                            ),
                        dmc.Group(
                            [
                                dmc.Button(
                                    "Personal Account",
                                    id="acc-button",
                                    leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled"),
                                    radius="xl",
                                    variant="outline",
                                    color="indigo"
                                ),
                                # dmc.Button(
                                #     "Twitter",
                                #     leftIcon=html.I(
                                #         className="fab fa-twitter fa-fw fa-lg"
                                #     ),
                                #     radius="xl",
                                #     variant="outline",
                                #     color="indigo"
                                # ),
                            ],
                            grow=True,
                            mt="1rem",
                            mb="1rem",
                        ),
                        dmc.Divider(
                            label="Or continue with email",
                            variant="dashed",
                            labelPosition="center",
                            mb="1.25rem",
                        ),
                        dmc.Stack(
                            [
                                dmc.TextInput(label="Email:"),
                                dmc.PasswordInput(label="Password:"),
                            ],
                            spacing="1rem",
                        ),
                        dmc.Group(
                            [
                                dcc.Link(
                                    dmc.Text(
                                        "Don't have an account? Register",
                                        color="gray",
                                        size="sm",
                                    ),
                                    href="/",
                                ),
                                # dmc.Button("Login", id="login-button", radius="md", color="indigo"),
                                html.A(
                                    "Login",
                                    href="http://127.0.0.1:7500",
                                    style={
                                        'display': 'inline-block',
                                        'text-align': 'center',
                                        'padding': '10px 20px',
                                        'background-color': '#4c6ef5',
                                        'color': 'white',
                                        'text-decoration': 'none',
                                        'border-radius': '5px',
                                        'font-size': '16px'
                                    }
                                )
                            ],
                            grow=True,
                            mt="1.5rem",
                            noWrap=True,
                            spacing="apart",
                        ),
                    ],
                    inheritPadding=True,
                )
            ],
            withBorder=True,
            shadow="xl",
            radius="lg",
            p="1.5rem",
            style={"width": "420px"},
        ),
        
        # dcc.Location(id='redirect-app', refresh=False)
    ],
)

# @app.callback(
#     Output('redirect-app', 'href'),
#     [Input('login-button', 'n_clicks')]
# )
# def redirect(n_clicks):
#     if n_clicks:
#         return "http://127.0.0.1:8000"  # Replace with the URL of your second Dash app
#     return ""


if __name__ == "__main__":
    app.run_server(debug=False, port=7654)
