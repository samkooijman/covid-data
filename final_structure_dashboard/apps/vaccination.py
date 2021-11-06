import dash
import json
import pandas as pd
import numpy as np
import plotly.express as px  # (version 4.7.0 or higher)
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import datetime as dt
from datetime import datetime
from geojson_rewind import rewind
import plotly.graph_objects as go
import pathlib
from app import app

import time

#app = dash.Dash()

def transpose(x):
    new = np.zeros(shape=(3,3))
    for date in x['date']:
        temp = x[x['date'] == date].T.iloc[2:].reset_index()
        temp['date'] = date
        temp = temp.to_numpy()
        new = np.append(new, temp, axis=0)
    df = pd.DataFrame(data=new, columns=['region', 'vaccination_coverage', 'date'])
    return df.iloc[3:]

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../src").resolve()

#Reading all the files
df = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/full_usa_vacc.csv')
uk_regions = json.load(open(DATA_PATH.joinpath('uk_regions.json')))
df_infec_usa = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/usa_cases.csv')
uk_vac = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/uk_vaccination.CSV", delimiter=",")


#Preparing the UK vac Data
uk_vac = uk_vac.rename(columns={
    "full_vacc_south_west": "South West",
    "full_vacc_north_east": "North East",
    "full_vacc_wales": "Wales",
    "full_vacc_london": "London",
    "full_vacc_west_midlands": "West Midlands",
    "full_vacc_north_west": "North West",
    "full_vacc_east_midlands": "East Midlands",
    "full_vacc_scotland": "Scotland",
    "full_vacc_south_east": "South East",
    "full_vacc_north_ireland": "Northern Ireland",
    "full_vacc_east_of_england": "East",
    "full_vacc_yorkshire_and_the_humber": "Yorkshire and the Humber"
})

uk_vac = uk_vac.rename(columns={'weekly_period_end' : 'date'})
uk_vac['date'] = pd.to_datetime(uk_vac['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')
uk_vac = transpose(uk_vac)
uk_vac['vaccination_coverage'] = pd.to_numeric(uk_vac['vaccination_coverage'])
uk_vac = uk_vac.sort_values(by=['date'])
available_indicators = ['USA', 'UK','Denmark']


#Creating ID to map coordinates of the UK
state_id_map = {}
for feature in uk_regions["features"]:
    feature["id"] = feature["properties"]["objectid"]
    state_id_map[feature["properties"]["rgn19nm"]] = feature["id"]

uk_vac['id'] = uk_vac['region'].apply(lambda x: state_id_map[x])

print(uk_vac)

#Some cure to the wounding geojson file. This is due to bad UK coordinates file.
uk_regions = rewind(uk_regions, rfc7946=False)


#Reformating datetimes to Y/m/d -- Currently the best I have due to problems with sorting.
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')


df['series_complete_pop_pct'] = df['series_complete_pop_pct'].replace('', np.nan)
df = df.dropna(axis=0, subset=['series_complete_pop_pct'])

df = df.sort_values(by='date', ascending=True)
begin = "2020/12/27"

end = df.iloc[-1, 1]

print(end)

#We need to play with this
daterange = pd.date_range(start=begin, end=end, freq='D', closed='right')

#The slider cannot use the datetime64ns but has to use an integer (UNIX)
def unixTimeMillis(dt):
    ''' Convert datetime to unix timestamp '''
    return int(time.mktime(dt.timetuple()))

def unixToDatetime(unix):
    ''' Convert unix timestamp to datetime. '''
    return pd.to_datetime(unix,unit='s')

def getMarks(start, end, Nth=100):
    ''' Returns the marks for labeling.
        Every Nth value will be used.
    '''

    result = {}
    for i, date in enumerate(daterange):
        if(i%Nth == 1):
            # Append value to dict
            result[unixTimeMillis(date)] = str(date.strftime('%d/%m/%Y'))

    return result


#Create the app-layout
layout = html.Div(children=[
    html.Br(),
    html.H1('Vaccination coverage'),
    html.Br(),
        html.Div([
            html.Label('Date Slider', id='time-range-label'),
            dcc.Slider( #Create the slider
                id='year_slider-1',
                min = unixTimeMillis(daterange.min()),
                max = unixTimeMillis(daterange.max()),
                value = unixTimeMillis(daterange.min()),
                step= 86400 * 7,
                marks=getMarks(daterange.min(),
                            daterange.max()),

            ),
        ],
        style={'margin-top': '20'}
    ),
    html.Hr(),


            html.H3(id='output_container', children=[]),
            html.H4('Vaccination % in the USA per state' , style = {'textAlign': 'center'}),
            dcc.Graph(id='vacc_usa', figure={}),
            html.H4('Vaccination % in the UK per state' , style = {'textAlign': 'center'}),
            dcc.Graph(id='uk_vac', figure={})
])

print(uk_vac['date'])

#Calling back the inputs and the outputs. E.g. a graph is an output
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='vacc_usa', component_property='figure'),
     Output(component_id='uk_vac', component_property='figure')],
    [Input(component_id='year_slider-1', component_property='value')])

# def _update_time_range_label(year_range):
#     return 'From {} to {}'.format(unixToDatetime(year_range[0]),
#                                   unixToDatetime(year_range[1]))


#Create the graph
def update_graph(date):

    #Connect the dataframes together
    dff = df.copy()
    dff_uk_vac = uk_vac.copy()
    date = (datetime.utcfromtimestamp(date).strftime('%Y/%m/%d'))
    dff = dff[dff['date'] == date] #Connect slider with USA Vacc dataframe
    dff_uk_vac = dff_uk_vac[dff_uk_vac['date'] == date]  # Connect slider
    container = "The date chosen by user is: {}".format(date)

    #dff = dff[dff["Affected by"] == "series_complete_pop_pct"]

    # Plotly Express -- Create the graphs
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state',
        scope="usa",
        color='series_complete_pop_pct',
        hover_data=['series_complete_pop_pct'],
        color_continuous_scale='RdBu',
    )

    fig_uk_vac = px.choropleth(dff_uk_vac,
                         locations='id',
                         geojson=uk_regions,  # Conecting the coordinate file with the figure
                         color="vaccination_coverage",
                         hover_data=['region'],
                         scope='europe')

    fig_uk_vac.update_geos(fitbounds='locations', visible=False) #updating the figure so that only the UK is visible instead of Europe


    return container, fig, fig_uk_vac

if __name__ == '__main__':
    app.run_server(debug=True)