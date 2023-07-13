
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

# Assuming your data is in a dataframe named df
# df = pd.read_csv("your_data.csv")
df = pd.read_csv("csv/UN_WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.csv")

app = dash.Dash(__name__)

min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
step_size = max((max_year - min_year) // 10, 1)  # This will divide the year range into 10 steps or use 1 as a minimum step.



app.layout = html.Div([
    html.H1("Simple app", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div(id='ads', style={'width': '20%', 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': i, 'value': i} for i in df['Region_subregion_country_or_area'].unique()],
                value=['WORLD'],
                multi=True
            ),
            dcc.Dropdown(
                id='gender-dropdown',
                options=[
                    {'label': 'Male', 'value': 'Male_Population_as_of_1_July_thousands'},
                    {'label': 'Female', 'value': 'Female_Population_as_of_1_July_thousands'},
                    {'label': 'Total', 'value': 'Total_Population_as_of_1_July_thousands'}
                ],
                value=['Total_Population_as_of_1_July_thousands'],
                multi=True
            ),
            dcc.RangeSlider(
                id='year-slider',
                min=min_year,
                max=max_year,
                value=[min_year, max_year],
                marks={str(year): str(year) for year in range(min_year, max_year+1, step_size)}
            ),
            dcc.Graph(id='time-series-chart')
        ], style={'width': '75%', 'display': 'inline-block', 'padding': '0 20'})
    ]),

    html.H3("Source: United Nations, Department of Economic and Social Affairs, Population Division (2022). World Population Prospects 2022, Online Edition.", style={'textAlign': 'center'}),
    
    html.P(
        """
        Disclaimer: This web site contains data tables, figures, maps, analyses and technical notes from the current revision of the World Population Prospects. 
        These documents do not imply the expression of any opinion whatsoever from neither the authors of this website or the Secretariat of the United Nations concerning the legal status of any country, territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. 
        """, style={'textAlign': 'justify'}
    )
])


@app.callback(
    Output('time-series-chart', 'figure'),
    Input('country-dropdown', 'value'),
    Input('gender-dropdown', 'value'),
    Input('year-slider', 'value')
)
def update_graph(selected_countries, selected_genders, selected_years):
    fig = go.Figure()

    for country in selected_countries:
        for gender in selected_genders:
            filtered_df = df[(df['Region_subregion_country_or_area'] == country) &
                             (df['Year'] >= selected_years[0]) &
                             (df['Year'] <= selected_years[1])]

            fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df[gender],
                                     mode='lines', name=f'{country}-{gender}'))

    fig.update_layout(title='Population over Time', xaxis_title='Year',
                      yaxis_title='Population', yaxis_tickformat = '.1f')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)