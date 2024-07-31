# classnames for all layout
# for text
PPD_H1 = "ppd-h1"
PPD_H2 = "ppd-h2"
PPD_H5 = "ppd-h5"

########################################################################
########################################################################

# on web_layout.py

# main div for  all web
WEB_CONTAINER = "web-container"

# div navigation bar
NAVBAR = 'navbar'

# # div web maps
# MAP_ALL = 'map-all'

# div for maps container
MAP_CONTAINER = 'map-container'

# div tabs
MAIN_TABS = "main-tabs"
MAIN_TABLIST = "main-tablist"

# div tabspanel
# overview container
OVW_CONTAINER = "overview-container"
# production performance dashboard container
PPD_CONTAINER = "ppd-container"
# gng dashboard container
GNG_CONTAINER = "gng-container"
# cost analysis dashboard container
CAD_CONTAINER = "cad-container"

# # div production
# PPD_PRODUCTION_ALL = "ppd-production-all"

# div footer
FOOTER_WEB = 'footer-web'

########################################################################
########################################################################

# on web_maps components

# prev on web_layout.py
# MAP_CONTAINER = 'map-container'

# on wmaps_layout.py
MAP_WRAPPER = "map-wrapper"

# MAP_ALL_WRAPPER = 'map-all-wrapper'

# div left grid-side map
LEFT_SIDE_MAP = 'left-side-map'
# Consist of:
# Text title and summary
TITLE_SUMMARY_LAYOUT = 'title-summary-layout'
TITLE_BLOCK = 'title-block'
SUMMARY_BLOCK = 'summary-block'
# Filter map
MAP_ALL_FILTER = 'map-all-filter'

# div right grid-side map
# Consist of:
# Map Leaflet
MAP_LEAFLET = 'map-leaflet'

########################################################################
########################################################################

# on oveerview components
# prev on web_layout.py
# OVW_CONTAINER = 'overview-container'

# on overview_layout.py
OVW_WRAPPER = 'overview-wrapper'
OVW_FILTER = 'overview-filter'
OVW_ACCORDION_FILTER = 'overview-accordion-filter'
OVW_MAIN_CONTENT = 'overview-main-content'

# on block_multiselect_filter.py
OVW_MULTISELECT_WRAPPER = 'overview-multiselect-wrapper'
OVW_MULTISELECT_MULTISELECT = 'overview-multiselect-multiselect'
OVW_MULTISELECT_BUTTON = 'overview-multiselect-button'

# on from_date_datepicker_filter.py
OVW_FROM_DATE_PICKER_WRAPPER = 'overview-from-date-picker-wrapper'
OVW_FROM_DATE_PICKER_DATEPICKER = 'overview-from-date-picker-datepicker'
OVW_ALL_DATE_PICKER_CHECKBOX = 'overview-all-date-picker-checkbox'

# on to_date_datepicker_filter.py
OVW_TO_DATE_PICKER_WRAPPER = 'overview-to-date-picker-wrapper'
OVW_TO_DATE_PICKER_DATEPICKER = 'overview-to-date-picker-datepicker'
# OVW_ALL_DATE_PICKER_CHECKBOX = 'overview-all-date-picker-checkbox'

# on overview_summary_card.py
OVW_SUMMARY_CARD_WRAPPER = 'overview-summary-card-wrapper'
OVW_SC_CARDSECTION = 'overview-summary-card-cardsection'
OVW_SC_SIMPLEGRID = 'overview-summary-card-simplegrid'
OVW_SC_GROUP = 'overview-summary-card-group'
OVW_SC_CARD = 'overview-summary-card-card'

OVW_SC_ICON = 'overview-summary-card-icon'
OVW_SC_TITLE = 'overview-summary-card-title'
OVW_SC_TEXT = 'overview-summary-card-text'

# on average_production_month_graph.py
OVW_AVG_PRODUCTION_MONTH_GRAPH = 'ovw-avg-production-month-graph'

# on operator_well_counts_pie_chart.py
OVW_OPERATOR_WELL_COUNTS_PIE_CHART = 'ovw-operator-well-counts-pie-chart'

# on top_ranks_production_bar_chart.py
OVW_TOP_RANKS_DROPDOWN = 'ovw-top-ranks-dropdown'
OVW_TOP_RANKS_OIL_GAS_SUBPLOTS = 'ovw-top-ranks-oil-gas-subplots'

# on preview_data_table.py

OVW_PREVIEW_DATA_CONTAINER = 'ovw-preview-data-container'
OVW_SELECT_DATA_SEGCONTROL = 'ovw-select-data-segment-control'
OVW_PREVIEW_DATA_TABLE = 'ag-theme-alpine'

########################################################################
########################################################################
# on production_performance components

# prev on web_layout.py
# PPD_CONTAINER = "ppd-container"

# on production_performance_layout.py
# div main container for ppd

PPD_WRAPPER = "ppd-wrapper"

# PPD_MAIN_WRAPPER = "ppd-main-wrapper"

# div filter on left grid
# production performance filter
PPD_PRODUCTION_FILTER = "ppd-production-filter"
# production performance accordion filter
PPD_ACCORDION_FILTER = "ppd-accordion-filter"

# div main on right grid
PPD_MAIN_GRAPHS = "ppd-main-graphs"

########################################################################

# parts of filter
# on well_main_multiselect.py
PPD_MULTISELECT_WRAPPER = "ppd-multiselect-wrapper"
PPD_MULTISELECT_MULTISELECT = "ppd-multiselect-multiselect"
PPD_MULTISELECT_BUTTON = "ppd-multiselect-button"

# on from_date_picker.py
PPD_FROM_DATE_PICKER_WRAPPER = "ppd-from-date-picker-wrapper"
PPD_FROM_DATE_PICKER_DATEPICKER = "ppd-from-date-picker-datepicker"
PPD_ALL_DATE_PICKER_CHECKBOX = "ppd-all-date-picker-checkbox"

# on to_date_picker.py
PPD_TO_DATE_PICKER_WRAPPER = "ppd-to-date-picker-wrapper"
PPD_TO_DATE_PICKER_DATEPICKER = "ppd-to-date-picker-datepicker"
PPD_TO_DATE_PICKER_BUTTON = "ppd-to-date-picker-button"

########################################################################
# parts of production performance charts
# summary card on summary_card.py
PPD_SUMMARY_CARD_LEFT_GRID = "ppd-summary-card-left-grid"
PPD_SC_CARDSECTION_LEFT_GRID = "ppd-sc-cardsection-left-grid"
PPD_SC_SIMPLEGRID_LEFT_GRID = "ppd-sc-simplegrid-left-grid"
PPD_SC_GROUP_LEFT_GRID = "ppd-sc-group-left-grid"
PPD_SC_CARD_LEFT_GRID  = "ppd-sc-card-left-grid"
PPD_SC_TITLE_LEFT_GRID = "ppd-sc-title-left-grid"
PPD_SC_TEXT_LEFT_GRID  = "ppd-sc-text-left-grid"
PPD_SC_ICON_LEFT_GRID = "ppd-sc-icon-left-grid"


# on oil_rate_line_chart.py
PPD_OIL_RATE_LINE_CHART = "ppd-oil-rate-line-chart"
# (SOON) on forecasting_oil_rate_line_chart.py
# PPD_SECOND_CHART_LEFT_GRID = "ppd-second-chart-left-grid"

# on well_stats_subplots.py
PPD_WELL_STATS_SUBPLOTS = "ppd-well-stats-subplots"
# on water_injection_subplots.py
PPD_WATER_INJECTION_SUBPLOTS = "ppd-water-injection-subplots"
# on water_cut_gor_line_subplots.py
PPD_WATER_CUT_GOR_SUBPLOTS = "ppd-water-cut-gor-line-subplots"
# on oil_vs_water_subplots.py
PPD_OIL_VS_WATER_SUBPLOTS = "ppd-oil-vs-water-subplots"
# on dp_choke_size_vs_avg_dp_subplots.py
PPD_DP_CS_VS_AVG_DP_SUBPLOTS = "ppd-dp-cs-vs-avg-dp-subplots"

########################################################################
########################################################################
# on gng_analysis components

# prev on web_layout.py
# GNG_CONTAINER = "gng-container"

# on gng_layout.py
GNG_WRAPPER = "gng-wrapper"
GNG_MAIN_FILTER = "gng-main-filter"

GNG_WELL_LOG_ACCORDION_FILTER = "gng-well-log-accordion-filter"
GNG_WELLS_3D_ACCORDION_FILTER = "gng-wells-3d-accordion-filter"

GNG_MAIN_GRAPHS = "gng-main-graphs"
GNG_GRAPH_TITLE = "gng-graph-title"
GNG_COMPARISON_GRAPHS = "gng-comparison-graphs"

# on well_log_graph.py
GNG_WELL_LOG_GRAPHS = "gng-well-log-graphs"

# on lithology_distribution_3d_filter.py
GNG_LITH_3D_FILTER = "gng-lith-3d-filter"

# on lithology_distribution_3d_graph.py
GNG_LITH_3D_GRAPH = "gng-lith-3d-graph"

# on wells_3d_filter.py
GNG_WELLS_3D_FILTER = "gng-wells-3d-filter"

# on wells_3d_graph.py
GNG_WELLS_3D_GRAPH = "gng-wells-3d-graph"



########################################################################
########################################################################

# Zara Chatbot
# BUTTON
ZARA_FLOAT_BUTTON = 'zara-float-button'

#Card chat
ZARA_CARD_SECTION = 'zara-card-section'
ZARA_CARD_INTRO = 'zara-card-intro'
ZARA_CARD_TABLE = 'zara-card-table'

#Tab data
ZARA_TAB_SECTION = 'zara-tab-section'

#response
ZARA_RESPONSE_SECTION = 'zara-response-section'

#Profile Grid
ZARA_PROFILE_GRID = 'zara-profile-grid'

#Chat Input
ZARA_DIV_CHAT = 'zara-div-chat'
ZARA_CHAT_INPUT = 'zara-chat-input'
ZARA_CHAT_AREA = 'zara-chat-area'

#Submit button
ZARA_SUBMIT_BUTTON = 'zara-submit-button'

