from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 
from abc import ABC, abstractmethod

class WebPage:
	def __init__(self,name):
		self.__name = name
		self.__webAddress = "/" + name
	
	@abstractmethod
	def get_layout(self):
		pass

class GenderSeriesPage(WebPage):
	def __init__(self, name, datafile = "csv/UN_WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT_REV1.csv",
	      		gender_dropdown_options = [
							{'label': 'Male', 'value': 'Male_Population_as_of_1_July_thousands'},
							{'label': 'Female', 'value': 'Female_Population_as_of_1_July_thousands'},
							{'label': 'Total', 'value': 'Total_Population_as_of_1_July_thousands'}
						], gender_dropdown_default = ['Total_Population_as_of_1_July_thousands']):
		super().__init__(name)
		self.__df = pd.read_csv(datafile)
		self.__min_year = int(self.__df['Year'].min())
		self.__max_year = int(self.__df['Year'].max())
		self.__step_size = max((self.__max_year - self.__min_year) // 10, 1)  # This will divide the year range into 10 steps or use 1 as a minimum step.
		self.__gender_dropdown_options = gender_dropdown_options
		self.__gender_dropdown_default = gender_dropdown_default

	def get_layout(self):
		return html.Div([
			html.H1("Simple app", style={'textAlign': 'center'}),
			html.Div([
				html.Div(id='ads', style={'width': '20%', 'display': 'inline-block'}),
				html.Div([
					dcc.Dropdown(
						id='country-dropdown',
						options=[{'label': i, 'value': i} for i in self.__df['Region_subregion_country_or_area'].unique()],
						value=['WORLD'],
						multi=True
					),
					dcc.Dropdown(
						id='gender-dropdown',
						options = self.__gender_dropdown_options,
						value= self.__gender_dropdown_default,
						multi=True
					),
					dcc.RangeSlider(
						id='year-slider',
						min=self.__min_year,
						max=self.__max_year,
						value=[self.__min_year, self.__max_year],
						marks={str(year): str(year) for year in range(self.__min_year, self.__max_year+1, self.__step_size)}
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

	def plot_callback(self, app):
		@app.callback(
			Output('time-series-chart', 'figure'),
			Input('country-dropdown', 'value'),
			Input('gender-dropdown', 'value'),
			Input('year-slider', 'value'),
		)
		def update_graph(selected_countries, selected_genders, selected_years):
			fig = go.Figure()

			for country in selected_countries:
				for gender in selected_genders:
					filtered_df = self.__df[(self.__df['Region_subregion_country_or_area'] == country) &
									(self.__df['Year'] >= selected_years[0]) &
									(self.__df['Year'] <= selected_years[1])]

					fig.add_trace(go.Scatter(x=filtered_df['Year'], y=filtered_df[gender],
											mode='lines', name=f'{country}-{gender}'))

			fig.update_layout(title='Population over Time', xaxis_title='Year',
							yaxis_title='Population', yaxis_tickformat = '.1f')

			return fig