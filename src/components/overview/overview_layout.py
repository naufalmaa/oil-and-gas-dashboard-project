from dash import Dash, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import cns

from ...data.source import DataSource
from src.components.overview import (
    
    overview_summary_card,
    block_multiselect_filter,
    from_date_datepicker_filter,
    to_date_datepicker_filter,
    average_production_month_graph,
    operator_well_counts_pie_chart,
    top_ranks_production_subplots,
    preview_data_button,
    preview_data_table
)

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.OVW_WRAPPER,
        children=[
           # div ovw-production filter
            html.Div(
                className=cns.OVW_FILTER,
                children=[
                    dmc.Accordion(
                        value="summary filter",
                        radius=10,
                        variant="contained",
                        className=cns.OVW_ACCORDION_FILTER,
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "Summary Filter",
                                        icon=DashIconify(
                                            icon="ooui:text-summary-ltr", width=25
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        html.Div(
                                            children=[
                                                block_multiselect_filter.render(app, source),
                                                
                                                from_date_datepicker_filter.render(
                                                    app, source
                                                ),
                                                to_date_datepicker_filter.render(app, source),
                                            ]
                                        )
                                    ),
                                ],
                                value="summary filter",
                            )
                        ],
                    )
                ],
            ),
            # div ovw-main (content(5))
            html.Div(
                className=cns.OVW_MAIN_CONTENT,
                children=[
                    overview_summary_card.render(app, source),
                    average_production_month_graph.render(app, source),
                    operator_well_counts_pie_chart.render(app, source),
                    top_ranks_production_subplots.render(app, source),
                    # preview_data_button.render(app, source),
                    # preview_data_table.render(app, source),
                    
                ],
            ),
        ]    
    )