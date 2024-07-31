# import pandas as pd

# from datetime import datetime, date

# from dash import Dash, html
# import dash_mantine_components as dmc
# from dash.dependencies import Input, Output, State
# from dash_iconify import DashIconify

# from ...data.loader import ProductionDataSchema
# from ...data.source import DataSource 

# from .. import ids, cns


# def render(app: Dash, source: DataSource) -> html.Div:
    
#     test_data = pd.read_csv("data/csv/aceh_production_data_daily_ed.csv")
#     test_data["DATEPRD"] = pd.to_datetime(test_data["DATEPRD"])
    
#     @app.callback(
#         Output(ids.DATES_RANGESLIDER, "value", allow_duplicate=True),
#         Output(ids.FROM_DATE_DATEPICKER, "value", allow_duplicate=True),
#         Output(ids.TO_DATE_DATEPICKER, "value", allow_duplicate=True),
#         [
#             Input(ids.DATES_RANGESLIDER, "value"),
#         ],
#         State(ids.FROM_DATE_DATEPICKER, "value"),
#         State(ids.TO_DATE_DATEPICKER, "value")
#     )
    
#     def sync_date_range_slider(date_range_slider, from_date, to_date) -> list[str]:
#     # If date range slider is changed
#         dataframe = source.filter(from_date=from_date, to_date=to_date)
        
#         # If date range slider is changed
#         if date_range_slider is not None and from_date is not None and to_date is not None:
#             start_index, end_index = date_range_slider
#             selected_from_date = pd.to_datetime(from_date)
#             selected_to_date = pd.to_datetime(to_date)


#             # Update date range slider if it doesn't match the selected date range
#             if selected_from_date != pd.to_datetime(dataframe[ProductionDataSchema.DATE].iloc[start_index]) or selected_to_date != pd.to_datetime(dataframe[ProductionDataSchema.DATE].iloc[end_index]):
#                 updated_start_index = dataframe[dataframe[ProductionDataSchema.DATE] == selected_from_date].index[0]
#                 updated_end_index = dataframe[dataframe[ProductionDataSchema.DATE] == selected_to_date].index[0]
#                 return [updated_start_index, updated_end_index], from_date, to_date

#         # If date picker is changed
#         elif date_range_slider is None and from_date is not None and to_date is not None:
#             selected_from_date = pd.to_datetime(from_date)
#             selected_to_date = pd.to_datetime(to_date)
#             start_index = dataframe[dataframe[ProductionDataSchema.DATE] == selected_from_date].index[0]
#             end_index = dataframe[dataframe[ProductionDataSchema.DATE] == selected_to_date].index[0]
#             return [start_index, end_index], from_date, to_date

#         # If initial loading or all inputs are None
#         return [0, len(dataframe) - 1], None, None

#     return html.Div(
#         children=[
#             html.H5("Select Range of Date:"),
            
#             dmc.RangeSlider(
#                 id='date-range-slider',
#                 marks={i: date.strftime('%Y-%m-%d') for i, date in enumerate(test_data[ProductionDataSchema.DATE])},
#                 min=0,
#                 max=len(test_data) - 1,
#                 value=[0, len(test_data) - 1]
#             ),      
#         ]
#     )