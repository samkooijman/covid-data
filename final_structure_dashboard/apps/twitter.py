import calmap
import calplot
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from dash import Dash, dcc, html, Input, Output

import plotly.express as px
import plotly.graph_objects as go

df4 = pd.read_csv('https://raw.githubusercontent.com/samkooijman/covid-data/main/Sentiment%20and%20Prediction/denmarksentimentframe.csv')

x1 = df4.tweet_timestamp
y1 = df4.fear
y2 = df4.anger
y3 = df4.happiness
y4 = df4.sadness

print(df4.head())




x1 = df4.tweet_timestamp
y1 = df4.fear
y2 = df4.anger
y3 = df4.happiness
y4 = df4.sadness

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.fear, mode='lines', name='Fear'))
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.anger, mode='lines', name='Anger'))
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.happiness, mode='lines', name='Happiness'))
fig1.add_trace(go.Scatter(x=df4.tweet_timestamp, y= df4.sadness, mode='lines', name='Sadness'))


figure(figsize=(12, 15), dpi=80)
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.plot(x1, y4)
plt.legend(["fear ", "anger", "happiness", "sadness"])

fig1.show()

layout = html.Div(children=[
    html.Br(),
    html.H1('Twitter API Sentiment Analysis'),

    html.Hr(),
            dcc.Graph(figure=fig1)
])