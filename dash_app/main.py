'''
Filename: /home/andres/DataoftheWorld/dash_app/main.py
Path: /home/andres/DataoftheWorld/dash_app
Created Date: Thursday, July 20th 2023, 5:10:08 pm
Author: Andres Mejia

Copyright (c) 2023 worlddatainsight
'''

import dash
from DataPage import GenderSeriesPage
from dash import dcc, html
from dash.dependencies import Input, Output
from initialize_pages import initialize_pages

def define_callbacks(app, page_dict):
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

def initialize_layout(app, pages):
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

def main():
    app = dash.Dash(__name__, suppress_callback_exceptions = True)
    app.title = "Data"
    pages = initialize_pages()
     # Register callbacks
    for page in pages:
        page.plot_callback(app)
    page_dict = {page.get_url(): page for page in pages}
    initialize_layout(app, pages)
    define_callbacks(app, page_dict)
    return app

app = main()
server = app.server
