from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import appje, political_pref, income, density
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
                dbc.NavLink("Political KPI", href='/apps/political_pref', active="exact"),
                dbc.NavLink("Density KPI", href='/apps/density', active="exact"),
                dbc.NavLink("Income KPI", href='/apps/income', active="exact"),
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


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])


def display_page(pathname):
    if pathname == '/apps/appje':
        return appje.layout
    elif pathname == '/apps/political_pref':
        return political_pref.layout
    elif pathname == '/apps/density':
        return density.layout
    elif pathname == '/apps/income':
        return income.layout

        

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=False)