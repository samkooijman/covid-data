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
import plotly.graph_objects as go



PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../src").resolve()

#Reading all the files
df = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/final_structure_dashboard/src/political_preference_usa.csv")
df_uk = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/final_structure_dashboard/src/political_pref_uk.csv', delimiter=';')
df_denmark = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/code/political_pref_denmark.csv", delimiter=";")
uk_regions = json.load(open(DATA_PATH.joinpath('uk_regions.json')))
denmark_regions = json.load(open(DATA_PATH.joinpath('denmark_regions.json')))
available_indicators = ['USA', 'UK','Denmark']
#Creating ID to map coordinates of the UK
df_infec_uk = df_uk.replace(["East of England"], "East") #In the coordinates it was called East. I can change this later if necessary
x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

#Creating ID to map coordinates of the UK
state_id_map = {}
for feature in uk_regions["features"]:
    feature["id"] = feature["properties"]["objectid"]
    state_id_map[feature["properties"]["rgn19nm"]] = feature["id"]
df_uk = df_uk.replace({
  'Yorkshire and The Humber': 'Yorkshire and the Humber' 
})

df_uk['id'] = df_uk['region_name'].apply(lambda x: state_id_map[x])
#dont have approriate source to map denmark


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
df_infec_uk = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/code/full_uk_infec.csv')
denmark_vac = pd.read_csv("https://raw.githubusercontent.com/samkooijman/covid-data/main/Regressions/Datasets/denmark_vac1.csv", delimiter=",")
denmark_vac = denmark_vac.rename(columns={'municipality' : 'region', 'vacc_pct_municipality' : 'vaccination_coverage'})
denmark_vac = denmark_vac[['region', 'vaccination_coverage']]
#latest from static data
df2 = df2[df2['date'] == '01/10/2021']
df_infec_uk = df_infec_uk[df_infec_uk['date'] == '01/10/2021']
#graduality based on republicans 
df2['series_complete_pop_pct'] = df2['series_complete_pop_pct'].replace('', np.nan)
df2 = df2.dropna(axis=0, subset=['series_complete_pop_pct'])
avg_number = ' ' + str(df2['series_complete_pop_pct'].median())
df = df.groupby(['state', 'party']).sum()/df.groupby(['state']).sum() * 100
df = df.reset_index()
df = df[df.party == 'DEM']
df = df.merge(df2, on='state')
df = df.reset_index()
df_uk['result'] = df_uk['lab']/df_uk['valid_votes']
total_votes_denmark = df_denmark['Number of people'].max() * 0.01
df_denmark=df_denmark.loc[df_denmark['Political party'].isin(['A. The Social Democratic Party', 'B. The Danish Social-Liberal Party', 'C. The Conservative Peoples Party', 'D. The New Right', 'E. Klaus Riskær Pedersen'])]
df_denmark['Number of people'] = (df_denmark['Number of people']/ total_votes_denmark) * 100
# filter different party name based on country
df_uk['result'].loc[(df_uk['region_name'] != 'Northern Ireland')] = df_uk['lab']/df_uk['valid_votes'] * 100
df_uk['result'].loc[(df_uk['region_name'] == 'Northern Ireland')] = df_uk['dup']/df_uk['valid_votes'] * 100
df_infec_uk = df_infec_uk.rename(columns={"areaname": "region_name"})
df_uk = df_uk.merge(df_infec_uk, on='region_name')
avg_number_denmark= ' '+ str(denmark_vac['vaccination_coverage'].median())
avg_number_usa = ' ' + str(df2['series_complete_pop_pct'].median()) 
avg_number_uk = ' ' + str(df_infec_uk['cases_per_100k'].median()) 

layout = html.Div([ 
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Denmark'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
    ]),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column-2',
                options=[{'label': i, 'value': i} for i in df_denmark['Region']],
                value='1. GENTOFTE'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
    ]),
    html.H4(id='title', children=[]),
    html.B(id='container', children=[]),
    dcc.Graph(id='indicator-graphic'),
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Output('container',component_property='children'),
    Output('title',component_property='children'),
    Input('xaxis-column', 'value'),
    Input('xaxis-column-2', 'value')
    )

def update_graph(xaxis_column_name, region):
    vaccination = denmark_vac[denmark_vac['region'].str.upper() == region[3:]]['vaccination_coverage']
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
        ), "Gradual from 0% ( Republicans ) to 100% ( Democrats ) ",  "Average vaccination coverage in USA: " + avg_number_usa

    elif xaxis_column_name == 'UK':
          return  px.choropleth(
            data_frame=df_uk,
            locations='id',
            color_continuous_scale='RdBu',
            geojson=uk_regions, #Conecting the coordinate file with the figure
            color="result",
            hover_data=['region_name', 'result', 'cases_per_100k'],
            scope='europe').update_geos(fitbounds='locations', visible=False),"Gradual from 0% ( Centre-right ) to 100% ( Centre-left ) ",  "Avarage vaccination covarage in UK: " + avg_number_uk
    else:
      return px.bar(
        data_frame=df_denmark[df_denmark['Region'] == region],
        x="Political party", y="Number of people",
        labels={'Number of people':'votes in %'},
        color='Political party',
        height=500
        
    ), vaccination,  "Average vaccination coverage in Denmark: " + avg_number_denmark

if __name__ == '__main__':
    app.run_server(debug=True)