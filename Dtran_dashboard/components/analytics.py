from server import app

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

from dash.exceptions import PreventUpdate

import dash_trich_components as dtc

from components.home import HomePageLayout
from components.sandbox import SandBoxLayout
from flask import request

theme_toggle = dtc.ThemeToggle()

## It's the layout that will receive the content of analytics
AnalyticsLayout =  html.Div(html.Div([html.Div(id="analytics-output-content", 
                                        style={"margin": "0 auto"}, 
                                        className="width-100 bgColor padding16")], 
                                className="width-100"), 
                        style={"minHeight":"100vh"}, 
                        className="bgKing")

# It's the page manager, wher   e will be received the information about the path
@app.callback(Output('analytics-output-content', 'children'),
              [Input('url', 'pathname')],
              )
def display_page(pathname):

    analytics_href = ['sandbox', 'settings', 'exit']

    # Submit button condition
    if (pathname is None) or (pathname not in ["/analytics"] + [f"/analytics-{i}" for i in analytics_href]):
        return HomePageLayout()
    elif pathname in ['/analytics', '/analytics-home']:
        return HomePageLayout()
    elif pathname in ['/analytics-sandbox']:
        return SandBoxLayout()
    elif pathname in ['/analytics-exit']:
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        return html.Div([
            html.H1('Server Shutdown!')
        ])

    else:
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
                html.Div([dcc.Link("Click here to go back to Analytics main page", href="analytics")])
            ]
        )

