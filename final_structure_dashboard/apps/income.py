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

from app import app

# Functions
def transpose(x):
    new = np.zeros(shape=(3,3))
    for date in x['date']:
        temp = x[x['date'] == date].T.iloc[2:].reset_index()
        temp['date'] = date
        temp = temp.to_numpy()
        new = np.append(new, temp, axis=0)
    df = pd.DataFrame(data=new, columns=['region', 'vaccination_coverage', 'date'])
    return df.iloc[3:]

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


# Importing data
uk_income = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/uk_income1.csv", delimiter=",")
usa_income = pd.read_excel("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/usa_income.xlsx")
denmark_income = pd.read_excel("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/Denmark_income.xlsx")

uk_vac = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/uk_vaccination.CSV", delimiter=",")
usa_vac = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/vacc_usa.csv", delimiter=",")
denmark_vac = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/denmark_vac1.csv", delimiter=",")

# Prepping uk_income
uk_income = uk_income.reset_index()
uk_income = uk_income[['level_0','level_2']]
uk_income = uk_income.iloc[:-5]
new_header = uk_income.iloc[0]
uk_income = uk_income[1:]
uk_income.columns = new_header
uk_income = uk_income.rename(columns={"Countries and\nregions of the \nUK" : "region", "GDHI per \nhead (£)¹" : "income"})
uk_income['income'] = uk_income['income'].str.replace(',', '')
uk_income['income'] = uk_income['income'].astype({'income': 'float64'})

# To dollar
dollars = []
for pound in uk_income['income']:
    dollar = pound * 1.3635794
    dollars = dollars + [dollar]
uk_income['income'] = dollars

# Prepping usa_income
usa_income = usa_income.iloc[2:-3].reset_index()
new_header = usa_income.iloc[0]
usa_income = usa_income[1:]
usa_income.columns = new_header
usa_income = usa_income.rename(columns={'Name' : 'region', 'Median Household Income (2019)' : 'income'})
usa_income = usa_income[['region', 'income']]
usa_income['income'] = usa_income['income'].str[1:]
usa_income['income'] = usa_income['income'].str.replace(',', '')
usa_income['income'] = usa_income['income'].str.replace('$', '')
usa_income['income'] = usa_income['income'].astype({'income': 'float64'})

usa_income = usa_income.replace({
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

# Prepping denmark_income
denmark_income = denmark_income[['Unnamed: 7', 'Unnamed: 8']]
denmark_income = denmark_income[2:]
denmark_income = denmark_income.rename(columns={'Unnamed: 7': 'region', 'Unnamed: 8' : 'income' })\

# To dollar 
dollars = []
for krone in denmark_income['income']:
    dollar = krone * 0.15582071
    dollars = dollars + [dollar]
denmark_income['income'] = dollars

# Prepping uk_vac
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
    "full_vacc_east_of_england": "East of England",
    "full_vacc_yorkshire_and_the_humber": "Yorkshire and The Humber"
})

uk_vac = uk_vac.rename(columns={'weekly_period_end' : 'date'})
uk_vac['date'] = pd.to_datetime(uk_vac['date'], format='%d-%m-%Y')
uk_vac = transpose(uk_vac)
uk_vac['vaccination_coverage'] = pd.to_numeric(uk_vac['vaccination_coverage'])
uk_vac = uk_vac.sort_values(by=['date'])

# Prepping usa_vac
usa_vac = usa_vac.rename(columns=str.lower)
usa_vac = usa_vac.rename(columns={"location" : "state"})
usa_vac = usa_vac.iloc[: , [0, 2, 42]]
usa_vac['date'] = pd.to_datetime(usa_vac['date'])
usa_vac = usa_vac.groupby(['date', 'state'], as_index=False).sum()
usa_vac = usa_vac.rename(columns={'state' : 'region', 'series_complete_pop_pct' : 'vaccination_coverage'})

# Prepping denmark_vac
denmark_vac = denmark_vac.rename(columns={'municipality' : 'region', 'vacc_pct_municipality' : 'vaccination_coverage'})
denmark_vac = denmark_vac[['region', 'vaccination_coverage']]

# Renaming regions in denmark_vac 
keys = {}
for region in denmark_vac['region']: 
  keys[region] = ((process.extract(region, denmark_income['region'], limit=1)))

labels = [] 
for key in keys:
    label = keys[key][0][0]
    labels = labels + [label]

denmark_vac['region'] = labels

# Merging income with vac
uk_income = pd.merge(uk_income, uk_vac, on='region')
usa_income = pd.merge(usa_income, usa_vac, on='region')
denmark_income = pd.merge(denmark_income, denmark_vac, on='region')

# Compensating for change in datetime
uk_income['date'] = pd.to_datetime(uk_income['date'], format='%d-%m-%Y')

# Only make us of sundays
uk_income = onlysunday(uk_income)
usa_income = onlysunday(usa_income)

# Performing linear regression (results: coef, intersect, mean absolute error, p-value)
a, b, c, d = making_lists(uk_income, 'income', 'vaccination_coverage')
uk_income['coef'] = a
uk_income['intersect'] = b
uk_income['error_rate'] = c
uk_income['p_value'] = d

a, b, c, d = making_lists(usa_income, 'income', 'vaccination_coverage')
usa_income['coef'] = a
usa_income['intersect'] = b
usa_income['error_rate'] = c
usa_income['p_value'] = d

# Dashboard creation

begin = uk_vac['date'].iloc[1]
end = uk_vac['date'].iloc[-1]

print(begin)
print(end)

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
            result[unixTimeMillis(date)] = str(date.strftime('%d-%m-%Y'))

    return result

dff3 = denmark_income.copy()

scatterplot6 = px.scatter(
        data_frame=dff3,
        x="income",
        y="vaccination_coverage",
        hover_data=['region'],
        text="region",
        height=550
    )

# scatterplot6.add_trace(go.Scatter (x=dff3['income'], y= dff3['coef'] * dff3["income"] + dff3["intersect"], mode="lines"))
# scatterplot6.update_traces(textposition='top center')

layout = html.Div(children=[
    html.Br(),
    html.H1('Vaccination Rate USA'),
    html.Div(
        [
            html.Label('From 2020 to 2021', id='time-range-label'),
            dcc.Slider(
                id='date_slider_income',
                min = unixTimeMillis(daterange.min()),
                max = unixTimeMillis(daterange.max()),
                step= 86400 * 7, #days in unix time
                value = unixTimeMillis(daterange.max()),
                marks=getMarks(daterange.min(),
                            daterange.max()),
            ),
        ],
        style={'margin-top': '20'}
    ),
    html.Hr(),
            html.Div(id='output_container_income', children=[]),
            dcc.Graph(id='dff4', figure={}),
            dcc.Graph(id='dff5', figure={}),
            dcc.Graph(figure=scatterplot6)
])

uk_income['date'] = pd.to_datetime(uk_income['date'], format='%d-%m-%Y')

uk_income['date'] = pd.to_datetime(uk_income['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')
usa_income['date'] = pd.to_datetime(usa_income['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')
#denmark_income['date'] = pd.to_datetime(denmark_income['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')

@app.callback(
    [Output(component_id='output_container_income', component_property='children'),
    Output(component_id='dff4', component_property='figure'),
    Output(component_id='dff5', component_property='figure')],
    #Output(component_id='dff6', component_property='figure')],
    [Input(component_id='date_slider_income', component_property='value')]
)


# Linear regression UK and USA 
def graph(date):
    date = (datetime.utcfromtimestamp(date).strftime('%Y/%m/%d'))
    container3 = "The date chosen by user was: {}".format(date)
    dff1 = uk_income.copy()
    dff1 = dff1[dff1['date'] == date]
    dff2 = usa_income.copy()
    dff2 = dff2[dff2['date'] == date]
    dff3 = denmark_income.copy()
    
    scatterplot4 = px.scatter(
        data_frame=dff1,
        x="income",
        y="vaccination_coverage",
        hover_data=['region'],
        text="region",
        height=550
    )

    scatterplot4.add_trace(go.Scatter (x=dff1['income'], y= dff1["coef"] * dff1["income"] + dff1["intersect"], mode="lines"))
    scatterplot4.update_traces(textposition='top center')

    scatterplot5 = px.scatter(
        data_frame=dff2,
        x="income",
        y="vaccination_coverage",
        hover_data=['region'],
        text="region",
        height=550
    )

    scatterplot5.add_trace(go.Scatter (x=dff2['income'], y= dff2["coef"] * dff2["income"] + dff2["intersect"], mode="lines"))
    scatterplot5.update_traces(textposition='top center')

    # scatterplot6 = px.scatter(
    #     data_frame=dff3,
    #     x="income",
    #     y="vaccination_coverage",
    #     hover_data=['region'],
    #     text="region",
    #     height=550
    # )
    #
    # scatterplot6.add_trace(go.Scatter (x=dff3['income'], y= dff3["coef"] * dff3["income"] + dff3["intersect"], mode="lines"))
    # scatterplot6.update_traces(textposition='top center')

    return container3, scatterplot4, scatterplot5 #, scatterplot6

if __name__ == '__main__':
    app.run_server(debug=True)