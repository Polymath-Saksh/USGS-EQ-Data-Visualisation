import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

#Data Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv


def extract_subarea(place):
    return place[0]

def extract_area(place):
    return place[-1]

def extract_date(time):
    return str(time).split(' ')[0]

def extract_weekday(time):
    date = extract_date(time)
    return date + '-' + str(time.weekday())

def extract_hour(time):
    t = str(time).split(' ')
    return t[0] + '-' + t[1].split(':')[0] 
#Fetch data and clean it

def fetch_eq_data(period='daily', region='Worldwide', min_mag=1):
    source='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}.csv'

    #Set frequency of data
    if period == 'weekly':
        new_source = source.format('all_week')
    elif period == 'monthly':
        new_source = source.format('all_month')
    else:
        new_source = source.format('all_day')
    
    #Fetch data and extract relevant columns
    df_eq = pd.read_csv(new_source)
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
        df_eq[animation_frame_col]= df_eq.time.apply(extract_weekday)
    elif period == 'monthly':
        animation_frame_col = 'date'
        df_eq[animation_frame_col]= df_eq.time.apply(extract_date)
    else:
        animation_frame_col = 'hours'
        df_eq[animation_frame_col]= df_eq.time.apply(extract_hour)
    

    df_eq = df_eq.sort_values(by='time')

    return df_eq, center_lat, center_lon, animation_frame_col

# Create Visualizer

def visualize_eq_data(period='daily', region='Worldwide',min_mag=1):
    df_eq, center_lat, center_lon,animation_frame_col = fetch_eq_data(period = period, region = region, min_mag = min_mag)

    fig = px.scatter_mapbox(
        data_frame=df_eq,
        lat='latitude',
        lon='longitude',
        center=dict(lat=center_lat, lon=center_lon),
        size = 'mag',
        color = 'mag',
        hover_name = 'sub_area',
        zoom = 1,
        mapbox_style='carto-positron',
        animation_frame=animation_frame_col,
        title='Earthquakes'
    )

    fig.show()

    return None

visualize_eq_data()