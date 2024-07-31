import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import requests
import pandas as pd
import json

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of your app
app.layout = html.Div([
    dcc.Graph(id='live-price-chart'),
    dcc.Interval(
        id='interval-component',
        interval=10 * 60 * 1000,  # Update every 10 minutes
        n_intervals=0
    )
])

# Function to fetch live oil and gas price data
def fetch_live_data():
    try:
        url = "https://www.oil-price.net/api/1.0/petroleum_spot_price/brent"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
        return None

# Define a callback to update the chart
@app.callback(
    Output('live-price-chart', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_live_chart(n):
    # Fetch live data
    live_data = fetch_live_data()
    
    if live_data is None:
        # Handle the case when data retrieval fails
        return px.bar(pd.DataFrame({'date': [], 'oil': [], 'gas': []}), title='Live Oil and Gas Prices')
    
    # Create a DataFrame from the data
    df = pd.DataFrame([live_data])
    
    # Update the chart
    fig = px.bar(df, x='date', y=['oil', 'gas'], title='Live Oil and Gas Prices')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
