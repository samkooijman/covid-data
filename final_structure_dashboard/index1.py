from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import vaccination, political_pref, income, density, twitter, weatherapi, infections

#Creating the Sidebar Style
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

#Creating the sidebar and connect it with every KPI
sidebar = html.Div(
    [
        html.H2("COVID DATA", className="display-4"),
        html.Hr(),
        html.P(
            "COVID dashboard", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Vaccination KPI", href='/apps/appje', active="exact"),
                html.Br(),
                dbc.NavLink("Infection KPI", href='/apps/infection', active="exact"),
                html.Br(),
                dbc.NavLink("Political KPI", href='/apps/political_pref', active="exact"),
                html.Br(),
                dbc.NavLink("Population Density KPI", href='/apps/density', active="exact"),
                html.Br(),
                dbc.NavLink("Income KPI", href='/apps/income', active="exact"),
                html.Br(),
                dbc.NavLink("Twitter Sentiment Analysis KPI", href='/apps/twitter', active="exact"),
                html.Br(),
                dbc.NavLink("Weather API KPI", href='/apps/weatherapi', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div(id='page-content', children=[],
    style = CONTENT_STYLE
    )
])

#Callbacks for webpages
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

#Linking webpages to references and their python layout files
def display_page(pathname):
    if pathname == '/apps/appje':
        return vaccination.layout
    elif pathname == '/apps/infection':
        return infections.layout
    elif pathname == '/apps/political_pref':
        return political_pref.layout
    elif pathname == '/apps/density':
        return density.layout
    elif pathname == '/apps/income':
        return income.layout
    elif pathname == '/apps/twitter':
        return twitter.layout

    elif pathname == '/apps/weatherapi':
        return weatherapi.layout

        

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=False)