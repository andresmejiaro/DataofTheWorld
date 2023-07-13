
import dash
from DataPage import GenderSeriesPage

def main():
	app = dash.Dash(__name__)
	app.title = "Data"
	#page = GenderSeriesPage("population")
	page = GenderSeriesPage("lexpectancy",
			 gender_dropdown_options=[
				 {"label":"Male", "value": "Male_Life_Expectancy_at_Birth_years"},
				 {"label":"Female", "value": "Female_Life_Expectancy_at_Birth_years"},
				 {"label":"Total", "value": "Life_Expectancy_at_Birth_both_sexes_years"}
				 ],
				 gender_dropdown_default=["Life_Expectancy_at_Birth_both_sexes_years"])
	page.plot_callback(app)
	app.layout = page.get_layout()
	app.run_server(debug=True)

if __name__ == '__main__':
	main()