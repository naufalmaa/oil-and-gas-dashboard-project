from dash import html, dcc
import dash_mantine_components as dmc

def settings_layout():
    return html.Div(
        children=[
            dmc.Text("OpenAI API Key", size="md", weight=500),
            dmc.TextInput(id="input-api-key", placeholder="Enter your OpenAI API Key before continue to chat...", type="password"),
            dmc.Text("Select Model", size="md", weight=500, style={"margin-top": "20px"}),
            dcc.Dropdown(
                id="select-model",
                options=[
                    {"label": "GPT-3.5 Turbo", "value": "gpt-3.5-turbo"},
                    {"label": "GPT-4", "value": "gpt-4"},
                ],
                value="gpt-4",
                clearable=False,
                style={"width": "100%"}
            ),
            dmc.Button("Save Settings", id="save-settings", style={"margin-top": "20px"}),
            dcc.Store(id="stored-api-key"),
            dcc.Store(id="stored-model"),
        ]
    )
