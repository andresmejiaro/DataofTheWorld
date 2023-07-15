
import dash
from DataPage import GenderSeriesPage
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions = True)

app.title = "Data"

# Initialize pages
pages = [
	GenderSeriesPage("population"),
	GenderSeriesPage(
		"lexpectancy",
		gender_dropdown_options=[
			{"label":"Male", "value": "Male_Life_Expectancy_at_Birth_years"},
			{"label":"Female", "value": "Female_Life_Expectancy_at_Birth_years"},
			{"label":"Total", "value": "Life_Expectancy_at_Birth_both_sexes_years"}
		],
		gender_dropdown_default=["Life_Expectancy_at_Birth_both_sexes_years"]
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
		html.H1("Data Visualization", style={'textAlign': 'center'}),
		html.Div(id='page-content'),
		html.Div([
			dcc.Link('Go to Population page', href=pages[0].get_url()),
			html.Br(),
			dcc.Link('Go to Life Expectancy page', href=pages[1].get_url())
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

server = app.server

