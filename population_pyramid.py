import dash
import dash_docre_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(childeren=[html.H1(children = 'Hello World'),])

if __name__ == '__main__':
	app.run_server(debug = True)