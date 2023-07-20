'''
Filename: /home/andres/DataoftheWorld/dash_app/main.py
Path: /home/andres/DataoftheWorld/dash_app
Created Date: Wednesday, July 19th 2023, 11:51:07 pm
Author: andres

Copyright (c) 2023 Your Company
'''

import dash
from DataPage import GenderSeriesPage
from dash import dcc, html
from dash.dependencies import Input, Output

def main():
    app = dash.Dash(__name__, suppress_callback_exceptions = True)
    app.title = "Data"

    # Initialize pages
    pages = [
        GenderSeriesPage("population",Title = "Population in thousands"),
        GenderSeriesPage(
            "lexpectancy",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Life_Expectancy_at_Birth_years"},
                {"label":"Female", "value": "Female_Life_Expectancy_at_Birth_years"},
                {"label":"Total", "value": "Life_Expectancy_at_Birth_both_sexes_years"}
            ],
            gender_dropdown_default=["Life_Expectancy_at_Birth_both_sexes_years"], Title = "Life expectancy at birth"
        )
    ]

    # Register callbacks
    for page in pages:
        page.plot_callback(app)

    # Create a mapping from URLs to pages
    page_dict = {page.get_url(): page for page in pages}

    # Define the layout
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div([
            html.H1("World Data Insight", style={'textAlign': 'center'}),
            html.Div(id='page-content'),
            html.Div([
                element for page in pages for element in 
                [dcc.Link(f'Go to {page._title} page', href=page.get_url()), html.Br()]
            ]),
        ])
    ])

    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        # handle the page changes based on the URL
        if pathname in page_dict:
            return page_dict[pathname].get_layout()
    
    @app.callback(Output('url', 'pathname'),
              [Input('url', 'pathname')])
    def redirect(pathname):
        if pathname == "/":
            return "/population"
        else:
            return pathname  
        
    return app

app = main()
server = app.server
