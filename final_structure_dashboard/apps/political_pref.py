import datetime as dt
import json
import pathlib
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from geojson_rewind import rewind
import plotly.express as px
from app import app
import pandas as pd


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

#Reading all the files
df = pd.read_csv(DATA_PATH.joinpath("political_preference_usa.csv"))


available_indicators = ['USA', 'UK','Denmark']
df_uk = pd.read_csv(DATA_PATH.joinpath("political_pref_uk.csv"), error_bad_lines=False)
uk_regions = json.load(open(DATA_PATH.joinpath('uk_regions.json')))
#Creating ID to map coordinates of the UK
df_infec_uk = df_uk.replace(["East of England"], "East") #In the coordinates it was called East. I can change this later if necessary

#Creating ID to map coordinates of the UK
state_id_map = {}
for feature in uk_regions["features"]:
    feature["id"] = feature["properties"]["objectid"]
    state_id_map[feature["properties"]["rgn19nm"]] = feature["id"]

#df_uk['id'] = df_uk['country_name'].apply(lambda x: state_id_map[x])


df = df.replace({
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


#Some cure to the wounding geojson file. This is due to bad UK coordinates file.
uk_regions = rewind(uk_regions, rfc7946=False)

#dataprep
df2 = pd.read_csv(DATA_PATH.joinpath("full_usa_vacc.csv"))
df2 = df2[df2['date'] == '01/10/2021']
#graduality based on republicans 
df2['series_complete_pop_pct'] = df2['series_complete_pop_pct'].replace('', np.nan)
df2 = df2.dropna(axis=0, subset=['series_complete_pop_pct'])
avg_number = ' ' + str(df2['series_complete_pop_pct'].median())
df = df.groupby(['state', 'party']).sum()/df.groupby(['state']).sum() * 100
df = df.reset_index()
df = df[df.party == 'DEM']
df = df.merge(df2, on='state')
df = df.reset_index()
avg_vaccination = 'Avarage vaccination covarage in country'

layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='UK'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
    ]),
    html.H6(avg_vaccination),html.B(avg_number),
    html.P("Gradual from 0% ( Republicans ) to 100% ( Democrats ) "),
    dcc.Graph(id='indicator-graphic'),
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value')
    )

def update_graph(xaxis_column_name):
    if xaxis_column_name == 'USA':
          return px.choropleth(
            data_frame=df,
            locationmode='USA-states',
            locations='state',
            scope="usa",
            color='total_votes',
            color_continuous_scale='RdBu',
            range_color=[0,100],
            hover_data=['total_votes', 'series_complete_pop_pct'],
        )
    elif xaxis_column_name == 'UK':
           return px.choropleth(
            data_frame=df_uk,
            locations='id',
            geojson=uk_regions, #Conecting the coordinate file with the figure
            color="cases_per_100k",
            scope='europe').update_geos(fitbounds='locations', visible=False)
    else: 
       return px.choropleth(
                df_infec_uk,
                locations='ons_region_id',
                geojson=uk_regions,
                color="green",
                cope='europe').update_geos(fitbounds='locations', visible=False)
 



if __name__ == '__main__':
    app.run_server(debug=True)