import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.graph_objects as go

app = dash.Dash(__name__, prevent_initial_callbacks='initial_duplicate', suppress_callback_exceptions=True, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

# Sample data
data = pd.DataFrame({
    'date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'value': [i for i in range(365)]
})

app.layout = html.Div([
    html.H1('Date Range Slider and Date Pickers'),
    html.Div([
        html.Label('From Date'),
        dcc.DatePickerSingle(
            id='from-date-picker',
            display_format='YYYY-MM-DD'
        )
    ]),
    html.Div([
        html.Label('To Date'),
        dcc.DatePickerSingle(
            id='to-date-picker',
            display_format='YYYY-MM-DD'
        )
    ]),
    dcc.RangeSlider(
        id='date-range-slider',
        marks = {
        i: date.strftime('%Y-%m-%d') for i, date in enumerate(data['date'])
        if date.month in [3, 6, 9, 12] and date.day == 1  # Display marks for every quarter
        },
        min=0,
        max=len(data) - 1,
        value=[0, len(data) - 1]
    ),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('date-range-slider', 'value', allow_duplicate=True),
    Output('from-date-picker', 'date', allow_duplicate=True),
    Output('to-date-picker', 'date', allow_duplicate=True),
    Input('graph', 'clickData')
)
def update_slider_and_datepickers(click_data):
    if click_data:
        selected_date = pd.to_datetime(click_data['points'][0]['x'])
        start_index = data[data['date'] == selected_date].index[0]
        end_index = start_index  # Set end_index to the selected date
        return [start_index, end_index], selected_date.strftime('%Y-%m-%d'), selected_date.strftime('%Y-%m-%d')
    return dash.no_update, dash.no_update, dash.no_update

@app.callback(
    Output('date-range-slider', 'value', allow_duplicate=True),
    Output('from-date-picker', 'date', allow_duplicate=True),
    Output('to-date-picker', 'date', allow_duplicate=True),
    Input('date-range-slider', 'value'),
    State('from-date-picker', 'date'),
    State('to-date-picker', 'date')
)
def sync_date_range_slider(date_range_slider, from_date, to_date):
    # If date range slider is changed
    if date_range_slider is not None and from_date is not None and to_date is not None:
        start_index, end_index = date_range_slider
        selected_from_date = pd.to_datetime(from_date)
        selected_to_date = pd.to_datetime(to_date)

        # Update date range slider if it doesn't match the selected date range
        if selected_from_date != data['date'][start_index] or selected_to_date != data['date'][end_index]:
            updated_start_index = data[data['date'] == selected_from_date].index[0]
            updated_end_index = data[data['date'] == selected_to_date].index[0]
            return [updated_start_index, updated_end_index], from_date, to_date

    # If date picker is changed
    elif date_range_slider is None and from_date is not None and to_date is not None:
        selected_from_date = pd.to_datetime(from_date)
        selected_to_date = pd.to_datetime(to_date)
        start_index = data[data['date'] == selected_from_date].index[0]
        end_index = data[data['date'] == selected_to_date].index[0]
        return [start_index, end_index], from_date, to_date

    # If initial loading or all inputs are None
    return [0, len(data) - 1], None, None

@app.callback(
    Output('graph', 'figure'),
    Input('date-range-slider', 'value')
)
def update_graph(date_range):
    start_index, end_index = date_range

    # Filter data based on selected date range
    filtered_data = data.iloc[start_index:end_index + 1]

    # Create a line plot of the filtered data
    fig = go.Figure(data=go.Scatter(x=filtered_data['date'], y=filtered_data['value']))
    fig.update_layout(title='Data Visualization')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)