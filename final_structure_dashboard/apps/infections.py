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
df_infec_uk = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/full_uk_infec.csv')
uk_regions = json.load(open(DATA_PATH.joinpath('uk_regions.json')))
df_infec_uk = df_infec_uk.replace(["East of England"], "East") #In the coordinates it was called East. I can change this later if necessary
df_infec_usa = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/usa_cases.csv')


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
df_infec_usa['date'] = pd.to_datetime(df_infec_usa['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')

print(df_infec_usa.head())

df['series_complete_pop_pct'] = df['series_complete_pop_pct'].replace('', np.nan)
df = df.dropna(axis=0, subset=['series_complete_pop_pct'])

df = df.sort_values(by='date', ascending=True)
begin = df.iloc[1, 1]

end = df.iloc[-1, 1]

print(end)

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
    html.H1('Infection per 100k people'),
    html.Div(
        [
            html.Label('Date Slider', id='time-range-label'),
            dcc.Slider( #Create the slider
                id='year_slider',
                min = unixTimeMillis(daterange.min()),
                max = unixTimeMillis(daterange.max()),
                value = unixTimeMillis(daterange.max()),
                         #unixTimeMillis(daterange.max())],
                marks=getMarks(daterange.min(),
                daterange.max()),
                step= 86400 * 7, #days in unix time

            ),
        ],
        style={'margin-top': '20'}
    ),
    html.Hr(),


            html.H3(id='output_container-1', children=[]),
            html.H4('Infections per 100k people in the USA', style = {'textAlign': 'center'}),
            dcc.Graph(id='infec_usa', figure={}),
            html.H4('Infections per 100k people UK', style = {'textAlign': 'center'}),
            dcc.Graph(id='infec_uk', figure={})
])



#Calling back the inputs and the outputs. E.g. a graph is an output
@app.callback(
    [Output(component_id='output_container-1', component_property='children'),
     Output(component_id='infec_usa', component_property='figure'),
     Output(component_id='infec_uk', component_property='figure')],
    [Input(component_id='year_slider', component_property='value')])

#Create the graph
def update_graph(date):

    #Connect the dataframes together
    dff = df.copy()
    dff_usa_infec = df_infec_usa.copy()
    dff_uk = df_infec_uk.copy()
    date = (datetime.utcfromtimestamp(date).strftime('%Y/%m/%d'))
    dff = dff[dff['date'] == date] #Connect slider with USA Vacc dataframe
    dff_uk = dff_uk[dff_uk['date'] == date]
    dff_usa_infec = dff_usa_infec[dff_usa_infec['date'] == date]#Connect slider with UK Infec dataframe

    container = "The date chosen by user is: {}".format(date)



    # Plotly Express -- Create the graph

    fig_infec_usa = px.choropleth(
        data_frame=dff_usa_infec,
        locationmode='USA-states',
        locations='state',
        scope="usa",
        color='new_cases_per_100k',
        hover_data=['new_cases_per_100k'],
        color_continuous_scale='RdBu',
    )

    fig2 = px.choropleth(dff_uk,
                          locations='id',
                          geojson=uk_regions, #Conecting the coordinate file with the figure
                          color="cases_per_100k",
                          hover_data=['areaname'],
                          scope='europe')


    fig2.update_geos(fitbounds='locations', visible=False) #updating the figure so that only the UK is visible instead of Europe


    return container, fig_infec_usa, fig2, 

if __name__ == '__main__':
    app.run_server(debug=True)