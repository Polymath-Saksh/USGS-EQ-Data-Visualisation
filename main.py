import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

#Data Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv


def extract_subarea(place):
    return place[0]

def extract_area(place):
    return place[-1]

#Fetch data and clean it

def fetch_eq_data(period='daily', region='Worldwide', min_mag=1):
    source='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{?}.csv'

    #Set frequency of data
    if period == 'weekly':
        source = source.format('all_week')
    elif period == 'monthly':
        source = source.format('all_month')
    else:
        source = source.format('all_day')
    
    #Fetch data and extract relevant columns
    df_eq = pd.read_csv(source)
    df_eq = df_eq[['time','latitude','longitude','mag','place']]

    #Extract sub-areas in place cols

    place_list=df_eq.place.str.split(', ')

    df_eq['sub_area'] = place_list.apply(extract_subarea)
    df_eq['area']=place_list.apply(extract_area)
    df_eq = df_eq.drop('place',axis=1)

    #Filter data based on min magnitude
    if isinstance(min_mag, int) and min_mag > 0:
        df_eq = df_eq[df_eq.mag>=min_mag]
    else:
        df_eq = df_eq[df_eq.mag>0]

    df_eq['time'] = pd.to_datetime(df_eq.time)

    #Set lat and long to default if region is not in df
    if region in df_eq.area.to_list():
        df_eq = df_eq[df_eq['area']==region]
        max_mag = df_eq.mag.max()
        center_lat = df_eq[df_eq.mag==max_mag].latitude.values[0]
        center_lon = df_eq[df_eq.mag==max_mag].longitude.values[0]
    else:
        center_lat, center_lon = [54,15]

    #Set cols for animation frames
    #weekdays, dates, hours
    if period == 'weekly':
        animation_frame_col = 'weekday'
        df_eq[animation_frame_col]= df_eq.time # TBD
    
    
# Create Visualizer