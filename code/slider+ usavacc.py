import dash
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import datetime as dt
from datetime import datetime
import plotly.graph_objects as go

import time

app = dash.Dash()

df = pd.read_csv("full_usa_vacc.csv")

daterange = pd.date_range(start='2021',end='2021/10/05',freq='D')

df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y').dt.strftime('%Y/%m/%d')


df.sort_values(by='date')

print(df['date'])

#print(time.mktime(df['date']))

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
app.layout = html.Div(children=[
    html.H1('Range Slider Testing'),
    html.Div(
        [
            html.Label('From 2020 to 2021', id='time-range-label'),
            dcc.Slider( #Create the slider
                id='year_slider',
                min = unixTimeMillis(daterange.min()),
                max = unixTimeMillis(daterange.max()),
                value = unixTimeMillis(daterange.min()),
                         #unixTimeMillis(daterange.max())],
                marks=getMarks(daterange.min(),
                            daterange.max()),
            ),
        ],
        style={'margin-top': '20'}
    ),
    html.Hr(),


            html.Div(id='output_container', children=[]),
    #dcc.Graph(id='my-graph'),
            dcc.Graph(id='vacc_usa', figure={})
])

#Calling back the inputs and the outputs. E.g. a graph is an output
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='vacc_usa', component_property='figure')],
    [Input(component_id='year_slider', component_property='value')])

# def _update_time_range_label(year_range):
#     return 'From {} to {}'.format(unixToDatetime(year_range[0]),
#                                   unixToDatetime(year_range[1]))


#Create the graph
def update_graph(date):

    #Connect the dataframes together
    dff = df.copy()
    date = (datetime.utcfromtimestamp(date).strftime('%Y/%m/%d'))
    dff = dff[dff['date'] == date] #This should connect the keys of the slider with the data from the df


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

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
