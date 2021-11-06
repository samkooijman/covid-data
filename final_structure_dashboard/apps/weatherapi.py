import pandas as pd
from sklearn.model_selection import train_test_split
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from dash import Dash, dcc, html, Input, Output
import datetime
from datetime import datetime
import time
import plotly.express as px
from app import app
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def linear_regression(x, y):

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    coef = regressor.coef_

    y_pred = regressor.predict(X_test)
    error = metrics.mean_absolute_error(y_test, y_pred)

    #print(y_pred, error)


    return coef[0], regressor.intercept_, error, X_test, y_pred


#Reading csv from github foor denmark and usa
df_wea_den = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/weather/denmark/combined.csv')
infec_den = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/infec_denmark.csv')

df_wea_usa = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/weather/usa/combined.csv')
infec_usa = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/usa_cases.csv')

#Renaming columns
df_wea_den = df_wea_den.rename(columns={'location' : 'region'})
df_wea_den = df_wea_den.rename(columns={'date_time' : 'date'})
df_wea_usa = df_wea_usa.rename(columns={'date_time' : 'date'})
df_wea_usa = df_wea_usa.rename(columns={'location' : 'state'})

#Changing format
infec_den['date'] = pd.to_datetime(infec_den['date'], format='%d-%m-%Y')
df_wea_den['date'] = pd.to_datetime(df_wea_den['date'], format='%Y-%m-%d')

infec_usa['date'] = pd.to_datetime(infec_usa['date'], format='%d/%m/%Y')
df_wea_usa['date'] = pd.to_datetime(df_wea_usa['date'], format='%Y-%m-%d')

#Replacing values
df_wea_usa = df_wea_usa.replace({
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

#Merging csv files
dk_weather = pd.merge(df_wea_den, infec_den, on=['date', 'region'])
usa_weather = pd.merge(df_wea_usa, infec_usa, on=['date', 'state'])

#Dropping
dk_weather.drop('Unnamed: 0', inplace=True, axis=1)
usa_weather.drop('Unnamed: 0', inplace=True, axis=1)

#Dropping duplicates
dk_weather = dk_weather.drop_duplicates()
usa_weather = usa_weather.drop_duplicates()

#Creating linear regression
coef, intercept, error, X_test, y_pred = linear_regression(dk_weather["tempC"].values.reshape(-1, 1), dk_weather["confirmed_cases_per_100k"].values.reshape(-1, 1))

#Plotting visual for Denmark
fig, ax1 = plt.subplots()

#print(dk_weather.keys())

ax1.scatter(dk_weather["tempC"], dk_weather["confirmed_cases_per_100k"])
ax1.plot(X_test.ravel(), y_pred.ravel(), "r")
#plt.show()

#Creating linear regression
coef2, intercept2, error2, X_test2, y_pred2 = linear_regression(usa_weather["tempC"].values.reshape(-1, 1), usa_weather["new_cases_per_100k"].values.reshape(-1, 1))

#Plotting visual for Denmark
fig2, ax2 = plt.subplots()

ax2.bar(usa_weather["tempC"], usa_weather["new_cases_per_100k"])
ax2.plot(X_test2.ravel(), y_pred2.ravel(), "r")



#Creating a datarange
begin = dk_weather['date'].iloc[1]
end = dk_weather['date'].iloc[-1]
daterange = pd.date_range(start=begin, end=end, freq='D', closed='right')


#The slider cannot use the datetime64ns but has to use an integer (UNIX)
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

#Creating the denmark weather scatterplot
dff7 = dk_weather.copy()
scatterplot7 = px.scatter(
        data_frame=dff7,
        x="tempC",
        y="confirmed_cases_per_100k",
        #hover_name='region',
        hover_data=['region', 'date'],
        #text="region",
        height=550
    )

scatterplot7.add_trace(go.Scatter (x=X_test.ravel(), y= y_pred.ravel(), mode="lines", name="Regression Line"))
scatterplot7.update_traces(textposition='top center')
scatterplot7.update_layout(xaxis_title='Temperature in Celsius', yaxis_title='Amount of infections per 100k people')


#Creating the layout + slider
layout = html.Div(children=[
    html.Br(),
    html.H1('Weather influences on the amount of infections'),
    html.Div(
        [
            html.Label('Date Slider', id='time-range-label'),
            dcc.Slider(
                id='date_slider_weather',
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
            html.H3(id='output_container_twitter', children=[]),
            html.H4('Weather influence on infections in Denmark', style = {'textAlign': 'center'}),
            dcc.Graph(figure=scatterplot7),
            html.H4('Weather influence on infections in the USA', style = {'textAlign': 'center'}),
            dcc.Graph(id='dff8', figure={})

])

#Changing the format of the dates
dk_weather['date'] = pd.to_datetime(dk_weather['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')
usa_weather['date'] = pd.to_datetime(usa_weather['date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')


#Calling back the slider with the graphs so that they'll connect with each other
@app.callback(
    [Output(component_id='output_container_twitter', component_property='children'),
     Output(component_id='dff8', component_property='figure')],
    [Input(component_id='date_slider_weather', component_property='value')]
)


#Creating the scatterplot of the USA weather regression
def graph(date):
    dff8 = usa_weather.copy()
    date = (datetime.utcfromtimestamp(date).strftime('%Y/%m/%d'))
    container4 = "The date chosen by the user is: {}".format(date)
    dff8 = dff8[dff8['date'] == date]

    scatterplot8 = px.scatter(
        data_frame=dff8,
        x="tempC",
        y="new_cases_per_100k",
        hover_name='state',
        hover_data=['state', 'date', ],
        #text="region",
        height=550
    )

    scatterplot8.add_trace(go.Scatter(x=X_test2.ravel(), y=y_pred2.ravel(), mode="lines", name="Regression Line"))
    scatterplot8.update_traces(textposition='top center')
    scatterplot8.update_layout(xaxis_title='Temperature in Celsius', yaxis_title='Amount of infections per 100k people')

    return container4, scatterplot8