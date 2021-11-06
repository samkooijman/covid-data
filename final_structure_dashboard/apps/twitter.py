
import pandas as pd

from dash import Dash, dcc, html, Input, Output


import plotly.graph_objects as go

#Reading the cleaned data
df4 = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/Sentiment%20and%20Prediction/denmarksentimentframe.csv')
df5 = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/Sentiment%20and%20Prediction/UKsentimentframe.csv')


#Creating the sentiment analysis plot for Denmark
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.fear, mode='lines', name='Fear'))
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.anger, mode='lines', name='Anger'))
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.happiness, mode='lines', name='Happiness'))
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.sadness, mode='lines', name='Sadness',))
fig1.update_layout(xaxis_title='Date', yaxis_title='Sentiment score')


#Creating the sentiment analysis plot for the UK
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df5.tweet_timestamp, y= df5.fear, mode='lines', name='Fear'))
fig2.add_trace(go.Scatter(x=df5.tweet_timestamp, y= df5.anger, mode='lines', name='Anger'))
fig2.add_trace(go.Scatter(x=df5.tweet_timestamp, y= df5.happiness, mode='lines', name='Happiness'))
fig2.add_trace(go.Scatter(x=df5.tweet_timestamp, y= df5.sadness, mode='lines', name='Sadness',))
fig2.update_layout(xaxis_title='Date', yaxis_title='Sentiment score')

#Basic layout with the constructed graphs
layout = html.Div(children=[
    html.Br(),
    html.H1('Twitter API Sentiment Analysis'),

    html.Hr(),
            html.H3('Twitter API Sentiment Analysis of Denmark regarding the Covid-19 pandemic', style={'textAlign': 'center'}),
            dcc.Graph(figure=fig1),
            html.H3('Twitter API Sentiment Analysis of the UK regarding the Covid-19 pandemic', style={'textAlign': 'center'}),
            dcc.Graph(figure=fig2)
])