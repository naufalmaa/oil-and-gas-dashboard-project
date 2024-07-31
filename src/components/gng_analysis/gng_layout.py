from dash import Dash, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import cns

from ...data.source import DataSource
from src.components.gng_analysis import (
    well_log_filter, 
    well_log_graph,
    wells_3d_filter,
    wells_3d_graph,
    lithology_distribution_3d_filter,
    lithology_distribution_3d_graph
)


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.GNG_WRAPPER,
        children=[
            # div wl-main-filter
            html.Div(
                className=cns.GNG_MAIN_FILTER,
                children=[
                    
                    # well-log-filter
                    dmc.Accordion(
                        value="well-log filter",
                        radius=10,
                        variant="contained",
                        className=cns.GNG_WELL_LOG_ACCORDION_FILTER,
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "Well-Log Filter",
                                        icon=DashIconify(
                                            icon="octicon:graph-16", width=25
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        html.Div(
                                            children=well_log_filter.render(app, source)
                                        )
                                    ),
                                ],
                                value="well-log filter",
                            )
                        ],
                    ),
                    
                    #well-3d-graph filter
                    dmc.Accordion(
                        value="well-3d-graph filter",
                        radius=10,
                        variant="contained",
                        className=cns.GNG_WELLS_3D_ACCORDION_FILTER,
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "3D Graphs Filter",
                                        icon=DashIconify(
                                            icon="octicon:graph-16", width=25
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        html.Div(
                                            children=wells_3d_filter.render(app, source) 
                                                    + lithology_distribution_3d_filter.render(app, source)
                                        )
                                    ),
                                ],
                                value="well-3d-graph filter",
                            )
                        ],
                    )
                    
                ],
            ),
            
            # div main-graph
            html.Div(
                className=cns.GNG_MAIN_GRAPHS,
                children=[
                    html.H2("Well-Log",
                            className=cns.GNG_GRAPH_TITLE),
                    well_log_graph.render(app, source),
                    
                    html.H2("3D Well Feature Comparison", className=cns.GNG_GRAPH_TITLE),
                    
                    html.Div(
                        className=cns.GNG_COMPARISON_GRAPHS,
                        children=[
                            
                            wells_3d_graph.render(app, source),
                            lithology_distribution_3d_graph.render(app, source)
                            
                        ],
                    )
                    
                    
                ],
            ),
        ],
    )
