import dash_mantine_components as dmc
from dash import Dash, Output, Input, callback, html

app = Dash(
    __name__,
    prevent_initial_callbacks="initial_duplicate",
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.layout = html.Div(
    [
        dmc.MultiSelect(
            label="Select frameworks",
            placeholder="Select all you like!",
            id="framework-multi-select",
            value=["ng", "vue"],
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            style={"width": 400, "marginBottom": 10},
        ),
        dmc.Text(id="multi-selected-value"),
    ]
)


@callback(
    Output("multi-selected-value", "children"),
    
    Input("framework-multi-select", "value")
)
def select_value(value):
    if len(value) < 2:
        return "Select at least 2."
    else:
        return ", ".join(value)


if __name__ == "__main__":
    app.run_server(debug=True)
