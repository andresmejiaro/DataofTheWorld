#%%

import dash
from dash import dcc, html
import pandas as pd

#%%

population = pd.read_csv("/csv/UN_WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.csv")



app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1(children = 'Hello World'),], dcc.Dropdown(population.))



if __name__ == '__main__':
	app.run_server(debug = True, host = "0.0.0.0")