# Friso packages 
from numpy.core.fromnumeric import std
from numpy.core.numeric import roll
import pandas as pd
import numpy as np 

import datetime
import openpyxl
from scipy import stats
from pandas.core.window import rolling

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  
from sklearn import metrics

import matplotlib.pyplot as plt
from fuzzywuzzy import process

# Sam packages 
from numpy.core.fromnumeric import std
from numpy.core.numeric import roll
import pandas as pd
import numpy as np

import dash
import json
import pandas as pd
import numpy as np
import plotly.express as px  
from dash import Dash, dcc, html, Input, Output  
import datetime as dt
from datetime import datetime
import plotly.graph_objects as go
import pathlib

import time

import openpyxl
from scipy import stats
from pandas.core.window import rolling

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split  
from sklearn import metrics
from sklearn.utils.extmath import density

import matplotlib.pyplot as plt

from appje import app

# Functions
def dropdates(table):
    occurences = table['date'].value_counts()
    occurences = occurences.to_frame().reset_index()
    occurences = occurences[occurences['date'] < 5]
    for date in occurences['index']:
        table = table[table['date'] != date]
    return table

def linear_regression(x, y):
    x_ready = x.reshape((-1,1))

    X_train, X_test, y_train, y_test = train_test_split(x_ready, y, test_size=0.2, random_state=0) 

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    coef = regressor.coef_

    y_pred = regressor.predict(X_test)
    error = metrics.mean_absolute_error(y_test, y_pred)

    X_train = flatten_list(X_train)

    slope, intercept, r_value, p_value, std_err = stats.linregress(X_train, y_train)


    return coef[0], regressor.intercept_, error, p_value
     
def making_lists (a, b, c):
    coef = [] 
    intersect = []
    Mean_Absolute_Error = [] 
    p_value = [] 
    for d in a['date']:
       e = a[a['date'] == d ]
       f = e[b].values
       g = e[c].values 
       x, y, z, v = linear_regression(f, g)
       coef.append(x)
       intersect.append(y)
       Mean_Absolute_Error.append(z)
       p_value.append(v)
    return coef, intersect, Mean_Absolute_Error, p_value
       
def flatten_list (x):
    flat_list = []
    for sublist in x:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def onlysunday(x):
    x = x[x['date'].dt.day_name() == 'Sunday']
    return x


# Importing 
uk_density = pd.ExcelFile('https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/uk_density.xls')
usa_density = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/usa_density.csv", delimiter=",")
denmark_density = pd.read_excel("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/denmark_density.xlsx")

uk_infec = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/uk_infection.CSV", delimiter=",")
usa_infec = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/usa_cases.csv", delimiter=",")
denmark_infec = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/denmark_vac.CSV", delimiter=',')

usa_pop = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/pop_usa.csv",  delimiter=",")


# Prepping uk_density
uk_density = pd.read_excel(uk_density, 'MYE 5')
uk_density = uk_density[6:]
new_header = uk_density.iloc[0]
uk_density = uk_density[1:]
uk_density.columns = new_header
uk_density = uk_density.loc[(uk_density['Geography'] == 'Region')| (uk_density['Geography'] == 'Country')] 
uk_density = uk_density[['Name', '2020 people per sq. km']]
uk_density = uk_density.rename(columns={'Name' : 'region', '2020 people per sq. km' : 'density'})

# Renaming regions in uk_density
uk_density = uk_density.replace({
    "SOUTH WEST": "South West",
    "NORTH EAST": "North East",
    "WALES": "Wales",
    "LONDON": "London",
    "SCOTLAND": "Scotland",
    "WEST MIDLANDS": "West Midlands",
    "NORTH WEST": "North West",
    "EAST MIDLANDS": "East Midlands",
    "SCOTLAND": "Scotland",
    "WEST MIDLANDS": "West Midlands",
    "SOUTH EAST": "South East",
    "NORTHERN IRELAND": "Northern Ireland",
    "EAST": "East of England",
    "NORTHERN IRELAND": "Northern Ireland",
    "YORKSHIRE AND THE HUMBER" : "Yorkshire and The Humber",
    "UNITED KINGDOM" : "United Kingdom",
    "GREAT BRITAIN" : "Great Britain",
    "ENGLAND AND WALES" : "England and Wales",
    "ENGLAND" : "England"
})

# Prepping usa_density
usa_density = usa_density[['State', 'density']]
usa_density = usa_density.rename(columns={'State' : 'region'})

# Density in sq KM
densityKM = []
for mile in usa_density['density']:
    km = mile * 0.386102159 
    densityKM = densityKM + [km]
usa_density['density'] = densityKM

# Renaming region in usa_density
usa_density = usa_density.replace({
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
})

# Prepping denmark_density
denmark_density = denmark_density[['Region', 'Population density']]
denmark_density = denmark_density.rename(columns={'Region': 'region', 'Population density' : 'density'})

# Prepping uk_infec
uk_infec = uk_infec[['areaname', 'date', 'cases_per_100k']]
uk_infec = uk_infec.rename(columns={'areaname': 'region'})
uk_infec['date'] = pd.to_datetime(uk_infec['date'], format='%d/%m/%Y')

# Renaming regions in usa_pop
usa_pop = usa_pop.replace({
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
})

# Prepping usa_infec with usa_pop
usa_infec = usa_infec.iloc[: , [0, 1, 5]]
usa_infec = usa_infec.rename(columns={"submission_date" : "date"})

usa_pop = usa_pop.iloc[5 : , [4, 5]]
usa_pop = usa_pop.rename(columns={"NAME" : "state", "CENSUS2010POP" : "population"})

usa_infec = pd.merge(usa_pop, usa_infec, on='state')
usa_infec['date'] = pd.to_datetime(usa_infec['date'], format='%m/%d/%Y')
usa_infec = usa_infec.groupby(['date', 'state', 'new_case'], as_index=False).sum()
usa_infec['new_case'] = usa_infec['new_case'] / usa_infec['population'] * 100000
usa_infec = usa_infec.rename(columns={"new_case" : "cases_per_100k", "state" : "region"})
usa_infec = usa_infec[['region', 'date', 'cases_per_100k']]

# Prepping denmark_infec
denmark_infec = denmark_infec[['region', 'date', 'confirmed_cases_per_100k']]
denmark_infec = denmark_infec.rename(columns={'confirmed_cases_per_100k' : 'cases_per_100k'})
denmark_infec['date'] = pd.to_datetime(denmark_infec['date'], format='%d-%m-%Y')


# Merging
uk_density = pd.merge(uk_density, uk_infec, on='region')
usa_density = pd.merge(usa_density, usa_infec, on='region')
denmark_density = pd.merge(denmark_density, denmark_infec, on='region')

# sorting on date 
uk_density = uk_density.sort_values(by=['region','date'])
usa_density = usa_density.sort_values(by=['region','date'])
denmark_density = denmark_density.sort_values(by=['region','date'])

# Creating rolling average for new cases, over two weeks
uk_density['rolling_avg'] = uk_density.groupby('region')['cases_per_100k'].transform(lambda x: x.rolling(14, 1).mean())
usa_density['rolling_avg'] = usa_density.groupby('region')['cases_per_100k'].transform(lambda x: x.rolling(14, 1).mean())
denmark_density['rolling_avg'] = denmark_density.groupby('region')['cases_per_100k'].transform(lambda x: x.rolling(14, 1).mean())

# drop dates with too few entries 
uk_density = dropdates(uk_density)
usa_density = dropdates(usa_density)
denmark_density = dropdates(denmark_density)


# Only make us of sundays
uk_density = onlysunday(uk_density)
usa_density = onlysunday(usa_density)
denmark_density = onlysunday(denmark_density)

# Performing linear regression (results: coef, intersect, mean absolute error, p-value)

a, b, c, d = making_lists(uk_density, 'density', 'rolling_avg')
uk_density['coef'] = a
uk_density['intersect'] = b
uk_density['error_rate'] = c
uk_density['p_value'] = d

a, b, c, d = making_lists(usa_density, 'density', 'rolling_avg')
usa_density['coef'] = a
usa_density['intersect'] = b
usa_density['error_rate'] = c
usa_density['p_value'] = d

a, b, c, d = making_lists(denmark_density, 'density', 'rolling_avg')
denmark_density['coef'] = a
denmark_density['intersect'] = b
denmark_density['error_rate'] = c
denmark_density['p_value'] = d

# Dashboard creation

begin = uk_density['date'].iloc[1]
end = uk_density['date'].iloc[-1]

daterange = pd.date_range(start=begin, end=end, freq='D', closed='right')

def unixTimeMillis(dt):
    return int(time.mktime(dt.timetuple()))

def unixToDatetime(unix):
    return pd.to_datetime(unix,unit='s')

def getMarks(start, end, Nth=100):
    result = {}
    for i, date in enumerate(daterange):
        if(i%Nth == 1):
            # Append value to dict
            result[unixTimeMillis(date)] = str(date.strftime('%Y-%m-%d'))

    return result

layout = html.Div(children=[
    html.Br(),
    html.H1('Vaccination Rate USA'),
    html.Div(
        [
            html.Label('From 2020 to 2021', id='time-range-label'),
            dcc.Slider(
                id='date_slider',
                min = unixTimeMillis(daterange.min()),
                max = unixTimeMillis(daterange.max()),
                value = unixTimeMillis(daterange.max()),
                marks=getMarks(daterange.min(),
                            daterange.max()),
            ),
        ],
        style={'margin-top': '20'}
    ),
    html.Hr(),
            html.Div(id='output_container2', children=[]),
            dcc.Graph(id='nice', figure={})
])


@app.callback(
    [Output(component_id='output_container2', component_property='children'),
    Output(component_id='nice', component_property='figure')],
    [Input(component_id='date_slider', component_property='value')]
)

# Linear regression UK and USA 
def graph(date):
    date = (datetime.utcfromtimestamp(date).strftime('%Y-%m-%d'))
    container2 = "The date chosen by user was: {}".format(date)
    dff1 = uk_density.copy()
    dff1 = dff1[dff1['date'] == date]
    dff2 = usa_density.copy()
    dff2 = dff2[dff2['date'] == date]
    dff3 = denmark_density.copy()
    dff3 = dff3[dff3['date'] == date]

    scatterplot1 = px.scatter(
        data_frame=dff1,
        x="density",
        y="rolling_avg",
        hover_data=['region'],
        text="region",
        height=550
    )

    scatterplot1.add_trace(go.Scatter (x=dff1['density'], y= dff1["coef"] * dff1["density"] + dff1["intersect"], mode="lines"))
    scatterplot1.update_traces(textposition='top center')

    scatterplot2 = px.scatter(
        data_frame=dff2,
        x="density",
        y="rolling_avg",
        hover_data=['region'],
        text="region",
        height=550
    )

    scatterplot2.add_trace(go.Scatter (x=dff2['density'], y= dff2["coef"] * dff2["density"] + dff2["intersect"], mode="lines"))
    scatterplot2.update_traces(textposition='top center')

    scatterplot3 = px.scatter(
        data_frame=dff3,
        x="density",
        y="rolling_avg",
        hover_data=['region'],
        text="region",
        height=550
    )

    scatterplot3.add_trace(go.Scatter (x=dff3['density'], y= dff3["coef"] * dff3["density"] + dff3["intersect"], mode="lines"))
    scatterplot3.update_traces(textposition='top center')

    return container2, scatterplot1, scatterplot2, scatterplot3



