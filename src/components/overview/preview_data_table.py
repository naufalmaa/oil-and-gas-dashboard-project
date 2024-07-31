from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify
import dash_ag_grid as dag

from dash.exceptions import PreventUpdate

from ...data.source import DataSource
from ...data.loader import ProductionDataSchema

# from ..production_performance.multiselect_helper import to_multiselect_options
from .. import ids, cns
import random


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.PREVIEW_DATA_TABLE, "rowData", allow_duplicate=True),
        # Output(ids.MEMORY_OUTPUT, 'data', allow_duplicate=True),
        Output(ids.PREVIEW_DATA_TABLE, "columnDefs", allow_duplicate=True),
        Input(ids.SELECT_DATA_SEGCONTROL, "value")
        # prevent_initial_call=True
    )
    def create_table(data: str):

        df_production = source.df_production
        df_gor = source.create_pivot_table_date_avg(ProductionDataSchema.WATER_CUT_DAILY, ProductionDataSchema.GAS_OIL_RATIO)
        df_log = source.df_log
        gdf_blocks = source.gdf_blocks
        gdf_wells = source.gdf_wells
        
        production_columns = df_production.drop(columns=["MOVING_AVERAGE", "MOVING_AVERAGE_OIL", "MOVING_AVERAGE_WI", "WATER_CUT_DAILY", "GAS_OIL_RATIO"]).columns.to_list()
        gor_columns = df_gor.columns.to_list()
        log_columns = df_log.columns.to_list()
        blocks_columns = gdf_blocks.drop(columns=["tooltip","popup","geometry"]).columns.to_list()
        wells_columns = gdf_wells.drop(columns=["tooltip","popup","geometry"]).columns.to_list()
        
        # if data == "data_production":
        #     return df_production.to_dict("records"), [{"field": i} for i in production_columns]
        
        # elif data == "data_log":
        #     return df_log.to_dict("records"), [{"field": i} for i in log_columns]
        
        # elif data == "geodata_blocks":
        #     return gdf_blocks.drop(columns=["tooltip","popup","geometry"]).to_dict("records"),[{"field": i} for i in blocks_columns]
        
        # elif data == "geodata_wells":
        #     return gdf_wells.drop(columns=["tooltip","popup","geometry"]).to_dict("records"),[{"field": i} for i in wells_columns]
        
        # else:
        #     pass
        if data is None:
            raise PreventUpdate
            
        elif data == "data_production":
            return df_production.to_dict("records"), [{"field": i} for i in production_columns]
        
        elif data == 'data_gor':
            return df_gor.to_dict('records'), [{'field':i} for i in gor_columns]
        
        elif data == "data_log":
            return df_log.to_dict("records"), [{"field": i} for i in log_columns]
        
        elif data == "geodata_blocks":
            return gdf_blocks.drop(columns=["tooltip","popup","geometry"]).to_dict("records"),[{"field": i} for i in blocks_columns]
        
        elif data == "geodata_wells":
            return gdf_wells.drop(columns=["tooltip","popup","geometry"]).to_dict("records"),[{"field": i} for i in wells_columns]
        
        else:
            pass

    return html.Div(
        className="table-div",
        children=[
            html.H2("Preview Data Table",
            className=cns.GNG_GRAPH_TITLE),
            dmc.SegmentedControl(
                id=ids.SELECT_DATA_SEGCONTROL,
                className=cns.OVW_SELECT_DATA_SEGCONTROL,
                value="data_production",
                data=[
                    {"value": "data_production", "label": "Production Data"},
                    {'value': 'data_gor', 'label': 'Water Cut Daily Gas Ratio'},
                    {"value": "data_log", "label": "Log Data"},
                    {"value": "geodata_blocks", "label": "Blocks Data"},
                    {"value": "geodata_wells", "label": "Wells Data"},
                ],
                mt=10,
            ),
            dag.AgGrid(
                id=ids.PREVIEW_DATA_TABLE,
                className=cns.OVW_PREVIEW_DATA_TABLE,
                defaultColDef={
                    "resizeable": True,
                    "sortable": True,
                    "filter": True,
                },
                dashGridOptions={"pagination": False},
                style={"height": "400px"},
            )
        ],
    )
