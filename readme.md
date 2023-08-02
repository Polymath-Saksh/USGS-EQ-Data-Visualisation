# US Geospatial Data Visualization

## Background

This project is to build a web application that visualizes US geological data. The data is collected from the USGS (United States Geological Survey) API. The data is about earthquakes that occurred in the past 7 days. The data is updated every 5 minutes. The map is built using Leaflet that plots the data based on the longitude and latitude of the earthquake. The data markers reflect the magnitude of the earthquake by their size and depth of the earth quake by color. The legend provides context for the map data. The map also includes popups that provide additional information about the earthquake when a marker is clicked. The data markers are also clickable and will redirect the user to the USGS website for that specific earthquake for more information.

## Data Source

The USGS Website through the following links: 
### Monthly Earthquake Data
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv

### Weekly Earthquake Data
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv

### Daily Earthquake Data

https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv

## Requirements

- Run the command below to install the required packages

```python
pip install -r requirements.txt
```

- Internet connection is required to run the application (For retrieving the data from the USGS website)

## How to run the application

```python
python app.py
```

## Contributing

We welcome contributions! For bug fixes, issues or suggestions.If you find a bug, have a feature request, or want to improve the code, please feel free to open an issue or submit a pull request. Ensure to follow the contribution guidelines specified in the repository under the [LICENSE](LICENSE.md) section.

## License

This project is licensed under the MIT License. For details, refer to the [LICENSE.md](LICENSE.md) file.

Code snippets from Bootstrap are used in this project. The license for Bootstrap can be found in the [LICENSE-BOOTSTRAP.md](LICENSE-BOOTSTRAP.md) file.




Copyright (c) 2023 Saksham Kumar