const { Pool } = require('pg');
const Plotly = require('plotly.js-dist');

// Configure PostgreSQL connection
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'data_of_the_world',
  password: 'zaq12wsx',
  port: 5432, // Default PostgreSQL port
});

async function fetchAndPlotData() {
  try {
    // Connect to the database
    const client = await pool.connect();

    // Fetch data from the database
	const query = 'SELECT Region__subregion__country_or_area__,Year,Male_Population__as_of_1_July__thousands_,Female_Population__as_of_1_July__thousands_ FROM UN_World_population_prospect_2022';
	const result = await client.query(query);
	
	// Process the data
	const data = result.rows;
	
	// Group the data by region and year
	const dataByRegionYear = {};
	for (const row of data) {
	  const regionYearKey = `${row.Region__subregion__country_or_area__}-${row.Year}`;
	  if (!dataByRegionYear[regionYearKey]) {
		dataByRegionYear[regionYearKey] = {
		  males: [],
		  females: [],
		};
	  }
	  dataByRegionYear[regionYearKey].males.push(row.Male_Population__as_of_1_July__thousands_);
	  dataByRegionYear[regionYearKey].females.push(row.Female_Population__as_of_1_July__thousands_);
	}
	
	// Create traces for each region and year
	const traces = [];
	const dropdownMenu = [];
	let counter = 0;
	for (const [regionYearKey, populations] of Object.entries(dataByRegionYear)) {
	  const [region, year] = regionYearKey.split('-');
	  
	  traces.push({
		x: populations.males,
		y: populations.females,
		type: 'bar',
		orientation: 'h',
		name: 'Males',
		visible: counter === 0,  // Only the first trace is visible initially
	  });
	  traces.push({
		x: populations.females.map((value) => -value),  // Females are shown on the left side
		y: populations.females,
		type: 'bar',
		orientation: 'h',
		name: 'Females',
		visible: counter === 0,  // Only the first trace is visible initially
	  });
	
	  dropdownMenu.push({
		method: 'update',
		args: [{ visible: traces.map((_, i) => i === counter) }],  // Only the selected trace is visible
		label: `${region} (${year})`,
	  });
	
	  counter += 2;  // Increase the counter by 2 because we added 2 traces (males and females)
	}
	
	// Generate the plot using Plotly
	const layout = {
	  title: 'Population Pyramid',
	  xaxis: { title: 'Population (thousands)' },
	  yaxis: { title: 'Age Group' },
	  updatemenus: [{
		buttons: dropdownMenu,
	  }],
	};
	
	Plotly.newPlot('plot', traces, layout);
	}
}
