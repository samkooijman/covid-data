from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import appje, density, income


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('First Page |', href='/apps/appje'),
        dcc.Link('Second page |', href='/apps/test'),
        dcc.Link('Weather KPI |', href='/apps/weather'),
        dcc.Link('Twitter API KPI |', href='/apps/twitter'),
        dcc.Link('Density KPI |', href='/apps/density'),
        dcc.Link('Covid-19 Measures KPI |', href='/apps/measures'),
        dcc.Link('Income KPI |', href='/apps/income')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])


def display_page(pathname):
    if pathname == '/apps/appje':
        return appje.layout
    elif pathname == '/apps/test':
        return "Test"
    elif pathname == '/apps/income':
        return income.layout
    elif pathname == '/apps/weather':
        return "weather"
    elif pathname == '/apps/density':
        return density.layout
    elif pathname == '/apps/measures':
        return "measures"
    elif pathname == '/apps/twitter':
        return "twitter"
    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=False)