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

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../src").resolve()

#Reading all the files
df = pd.read_csv(DATA_PATH.joinpath("full_usa_vacc.csv"))
df_infec_uk = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/full_uk_infec.csv')
uk_regions = json.load(open(DATA_PATH.joinpath('uk_regions.json')))
df_infec_uk = df_infec_uk.replace(["East of England"], "East") #In the coordinates it was called East. I can change this later if necessary

#Creating ID to map coordinates of the UK
state_id_map = {}
for feature in uk_regions["features"]:
    feature["id"] = feature["properties"]["objectid"]
    state_id_map[feature["properties"]["rgn19nm"]] = feature["id"]

df_infec_uk['id'] = df_infec_uk['areaname'].apply(lambda x: state_id_map[x])


#Some cure to the wounding geojson file. This is due to bad UK coordinates file.
uk_regions = rewind(uk_regions, rfc7946=False)


#Reformating datetimes to Y/m/d -- Currently the best I have due to problems with sorting.
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')
df_infec_uk['date'] = pd.to_datetime(df_infec_uk['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')

df['series_complete_pop_pct'] = df['series_complete_pop_pct'].replace('', np.nan)
df = df.dropna(axis=0, subset=['series_complete_pop_pct'])

df = df.sort_values(by='date', ascending=True)
begin = df.iloc[1, 1]
end = df.iloc[-1, 1]

#We need to play with this
daterange = pd.date_range(start='2021', end=end, freq='D', closed='right')


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
    html.H1('Vaccination Rate USA'),
    html.Div(
        [
            html.Label('From 2020 to 2021', id='time-range-label'),
            dcc.Slider( #Create the slider
                id='year_slider',
                min = unixTimeMillis(daterange.min()),
                max = unixTimeMillis(daterange.max()),
                value = unixTimeMillis(daterange.max()),
                         #unixTimeMillis(daterange.max())],
                marks=getMarks(daterange.min(),
                            daterange.max()),
            ),
        ],
        style={'margin-top': '20'}
    ),
    html.Hr(),


            html.Div(id='output_container', children=[]),
            dcc.Graph(id='vacc_usa', figure={}),
            html.H1('Infections per 100k people UK'),
            dcc.Graph(id='infec_uk', figure={})
])

#Calling back the inputs and the outputs. E.g. a graph is an output
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='vacc_usa', component_property='figure'),
     Output(component_id='infec_uk', component_property='figure')],
    [Input(component_id='year_slider', component_property='value')])

# def _update_time_range_label(year_range):
#     return 'From {} to {}'.format(unixToDatetime(year_range[0]),
#                                   unixToDatetime(year_range[1]))


#Create the graph
def update_graph(date):

    #Connect the dataframes together
    dff = df.copy()
    dff_uk = df_infec_uk.copy()
    date = (datetime.utcfromtimestamp(date).strftime('%Y/%m/%d'))
    dff = dff[dff['date'] == date] #Connect slider with USA Vacc dataframe
    dff_uk = dff_uk[dff_uk['date'] == date]  #Connect slider with UK Infec dataframe

    container = "The date chosen by user was: {}".format(date)

    #dff = dff[dff["Affected by"] == "series_complete_pop_pct"]

    # Plotly Express -- Create the graph
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state',
        scope="usa",
        color='series_complete_pop_pct',
        hover_data=['series_complete_pop_pct'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )

    fig2 = px.choropleth(dff_uk,
                          locations='id',
                          geojson=uk_regions, #Conecting the coordinate file with the figure
                          color="cases_per_100k",
                          scope='europe')

    fig2.update_geos(fitbounds='locations', visible=False) #updating the figure so that only the UK is visible instead of Europe

    return container, fig, fig2

if __name__ == '__main__':
    app.run_server(debug=True)