from DataPage import GenderSeriesPage

def initialize_pages():
    pages = [
        GenderSeriesPage("population",Title = "Population in thousands"),
        
        GenderSeriesPage(
            "lexpectancy",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Life_Expectancy_at_Birth_years"},
                {"label":"Female", "value": "Female_Life_Expectancy_at_Birth_years"},
                {"label":"Total", "value": "Life_Expectancy_at_Birth_both_sexes_years"}
            ],
            gender_dropdown_default=["Life_Expectancy_at_Birth_both_sexes_years"], Title = "Life expectancy at birth"),
            
        GenderSeriesPage(
            "tdeaths",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Deaths_thousands"},
                {"label":"Female", "value": "Female_Deaths_thousands"},
                {"label":"Total", "value": "Total_Deaths_thousands"}
            ],
            gender_dropdown_default=["Total_Deaths_thousands"], Title = "Total deaths (thousands)"),
        
        GenderSeriesPage(
            "lexpectancy15",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Life_Expectancy_at_Age_15_years"},
                {"label":"Female", "value": "Female_Life_Expectancy_at_Age_15_years"},
                {"label":"Total", "value": "Life_Expectancy_at_Age_15_both_sexes_years"}
            ],
            gender_dropdown_default=["Life_Expectancy_at_Age_15_both_sexes_years"], Title = "Life expectancy at age 15"),
        
		GenderSeriesPage(
            "lexpectancy65",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Life_Expectancy_at_Age_65_years"},
                {"label":"Female", "value": "Female_Life_Expectancy_at_Age_65_years"},
                {"label":"Total", "value": "Life_Expectancy_at_Age_65_both_sexes_years"}
            ],
            gender_dropdown_default=["Life_Expectancy_at_Age_65_both_sexes_years"], Title = "Life expectancy at age 65"),
        
		GenderSeriesPage(
            "lexpectancy80",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Life_Expectancy_at_Age_80_years"},
                {"label":"Female", "value": "Female_Life_Expectancy_at_Age_80_years"},
                {"label":"Total", "value": "Life_Expectancy_at_Age_80_both_sexes_years"}
            ],
            gender_dropdown_default=["Life_Expectancy_at_Age_80_both_sexes_years"], Title = "Life expectancy at age 80"),
        
		GenderSeriesPage(
            "mortality40",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Mortality_before_Age_40_deaths_under_age_40_per_1000_male_live_births"},
                {"label":"Female", "value": "Female_Mortality_before_Age_40_deaths_under_age_40_per_1000_female_live_births"},
                {"label":"Total", "value": "Mortality_before_Age_40_both_sexes_deaths_under_age_40_per_1000_live_births"}
            ],
            gender_dropdown_default=["Mortality_before_Age_40_both_sexes_deaths_under_age_40_per_1000_live_births"], 
            Title = "Mortality under age 40 per 1000 live births"),

		GenderSeriesPage(
            "mortality60",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Mortality_before_Age_60_deaths_under_age_60_per_1000_male_live_births"},
                {"label":"Female", "value": "Female_Mortality_before_Age_60_deaths_under_age_60_per_1000_female_live_births"},
                {"label":"Total", "value": "Mortality_before_Age_60_both_sexes_deaths_under_age_60_per_1000_live_births"}
            ],
            gender_dropdown_default=["Mortality_before_Age_60_both_sexes_deaths_under_age_60_per_1000_live_births"], 
            Title = "Mortality under age 60 per 1000 live births"),
            
        GenderSeriesPage(
            "mortality15-50",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Mortality_between_Age_15_and_50_deaths_under_age_50_per_1000_males_alive_at_age_15"},
                {"label":"Female", "value": "Female_Mortality_between_Age_15_and_50_deaths_under_age_50_per_1000_females_alive_at_age_15"},
                {"label":"Total", "value": "Mortality_between_Age_15_and_50_both_sexes_deaths_under_age_50_per_1000_alive_at_age_15"}
            ],
            gender_dropdown_default=["Mortality_between_Age_15_and_50_both_sexes_deaths_under_age_50_per_1000_alive_at_age_15"],
            Title = "Mortality between Age 15 and 50. Deaths under age 50 per 1000 alive at age 15"),
        
		GenderSeriesPage(
            "mortality15-60",
            gender_dropdown_options=[
                {"label":"Male", "value": "Male_Mortality_between_Age_15_and_60_deaths_under_age_60_per_1000_males_alive_at_age_15"},
                {"label":"Female", "value": "Female_Mortality_between_Age_15_and_60_deaths_under_age_60_per_1000_females_alive_at_age_15"},
                {"label":"Total", "value": "Mortality_between_Age_15_and_60_both_sexes_deaths_under_age_60_per_1000_alive_at_age_15"}
            ],
            gender_dropdown_default=["Mortality_between_Age_15_and_60_both_sexes_deaths_under_age_60_per_1000_alive_at_age_15"],
            Title = "Mortality between Age 15 and 60. Deaths under age 60 per 1000 alive at age 15"),
	            
    ]
    return pages