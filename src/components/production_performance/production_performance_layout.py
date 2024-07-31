
from dash import Dash, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import cns

from ...data.source import DataSource
from src.components.production_performance import (
    
    summary_card,
    oil_rate_line_chart,
    forecasting_oil_rate_line_chart,
    well_stats_subplots,
    water_injection_subplots,
    water_cut_gor_line_subplots,
    oil_vs_water_subplots,
    dp_choke_size_vs_avg_dp_subplots,
    
    well_main_multiselect,
    from_date_datepicker,
    to_date_datepicker
)

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.PPD_WRAPPER,
        children=[
           # div ppd-production filter (content{4})
            html.Div(
                className=cns.PPD_PRODUCTION_FILTER,
                children=[
                    dmc.Accordion(
                        value="production filter",
                        radius=10,
                        variant="contained",
                        className=cns.PPD_ACCORDION_FILTER,
                        children=[
                            dmc.AccordionItem(
                                [
                                    dmc.AccordionControl(
                                        "Well Production Filter",
                                        icon=DashIconify(
                                            icon="octicon:graph-16", width=25
                                        ),
                                    ),
                                    dmc.AccordionPanel(
                                        html.Div(
                                            children=[
                                                well_main_multiselect.render(
                                                    app, source
                                                ),
                                                from_date_datepicker.render(
                                                    app, source
                                                ),
                                                to_date_datepicker.render(app, source),
                                            ]
                                        )
                                    ),
                                ],
                                value="production filter",
                            )
                        ],
                    )
                ],
            ),
            # div ppd-main-graph (content(5))
            html.Div(
                className=cns.PPD_MAIN_GRAPHS,
                children=[
                    summary_card.render(app, source),
                    oil_rate_line_chart.render(app, source),
                    well_stats_subplots.render(app, source),
                    water_injection_subplots.render(app, source),
                    water_cut_gor_line_subplots.render(app, source),
                    oil_vs_water_subplots.render(app, source),
                ],
            ),
        ]    
    )