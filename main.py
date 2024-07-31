from dash import Dash, html, Input, Output
import dash.exceptions

from src.components.web_layout import create_layout
from src.data.loader import load_well_production_data, load_all_blocks, load_all_wells, load_log_data
from src.data.source import DataSource

PRODUCTION_DATA_PATH = "./data/csv/aceh_production_data_daily_rev.csv"
BLOCK_DATA_PATH = './data/geojson/all_blocks_rev.geojson'
WELL_DATA_PATH = './data/geojson/all_wells_rev.geojson'
LOG_DATA_PATH = "./data/csv/aceh_log_data_rev.csv"

def main() -> None: 
    
    data_well = load_well_production_data(PRODUCTION_DATA_PATH)
    geodata_block = load_all_blocks(BLOCK_DATA_PATH)
    
    # 150823
    geodata_well = load_all_wells(WELL_DATA_PATH)
    
    # 040823
    data_log = load_log_data(LOG_DATA_PATH) 
    data = DataSource(_data=data_well, _geodata_blocks=geodata_block, _geodata_wells=geodata_well, _data_log=data_log)
    
    app = Dash(__name__, prevent_initial_callbacks='initial_duplicate', suppress_callback_exceptions=True, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ])
    
    app.title = "Dashboad Project"
    app.layout = create_layout(app, data)

    app.run_server(
        debug=False, 
        port = 7500)

if __name__ == '__main__':
    main()