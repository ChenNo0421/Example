# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:11:12 2023

@author: robert
"""

import random 

from dash import dcc
from dash              import html, dcc, no_update
from datetime import datetime


def scatter(id_new, new_title, interval_value, chart_type, x=None, y=None):
    
    dt = [
            {'x': ['a', 'b', 'c'], 'y': [4, 1, 2], 'type': chart_type, 'name': random.choice(['Brazil', 'US', 'Australia', 'Nigeria', 'China', 'India'])},
            {'x': ['a', 'b', 'c'], 'y': [3, 6, 1], 'type': chart_type, 'name': random.choice(['Argentina', 'Cuba', 'Russia', 'France', 'Spain'])}
            ]
    
    if x is not None and y is not None:
        
        x = [datetime.strptime(t, "%d/%m/%Y %H:%M:%S") for t in x]
        dt = [{'x': x, 'y': y, 'type': chart_type}]

    content = dcc.Graph(
        id={"type": "graph", "index":id_new},
        figure={
            'data': dt,
            'layout': 
            {
                'title': new_title + " " + str(interval_value),
                'margin':dict(l=40, r=25, t=40),
                'autosize': True,
                "plot_bgcolor":"#444",
                "paper_bgcolor":"#444",
                'font': {'color': "white"}
            },
            
        },
        config={
                'autosizable': True,
                'doubleClick': 'autosize',
                'frameMargins': 0,
                'displaylogo': False,
                'editable': True},
        style={
            "height":"100%",
            "width":"100%"})
        
    return content

def pie(id_new, new_title, interval_value):
    content = dcc.Graph(
        id={"type": "graph", "index":id_new},
        figure={
            'data':
            [
                {'labels': ['a', 'b', 'c'], 
                 'values': [4, 1, 2], 
                 'type': 'pie',
                 'hole': .3, 
                 'name': 'pie',
                 'sort': True},
            ],
            'layout': 
            {
                #'title': new_title + " " + str(interval_value),
                'margin':dict(l=10, r=20, b=10, t=40),
                'autosize': True,
                "plot_bgcolor":"#444",
                "paper_bgcolor":"#444",
                'font': {'color': "white"}
            },
            
        },
        config={
                'autosizable': True,
                'frameMargins': 0,
                'displaylogo': False,
                'editable': True
                },
        style={"width":"100%"})
        
    return content

def table(id_new, new_title, interval_value):
    content = dcc.Graph(
        id={"type": "graph", "index":id_new},
        figure={
            'data':
            [
                {'type': 'table',
                 'header':{
                     'values': ['a', 'b', 'c'],
                     'line': {'color': 'white'}
                     },
                 'cells': {
                     'values': ['one', 'two', 'eric'],
                     'fill': {'color': '#444'},
                     'font': {'color': 'white'},
                     'line': {'color': 'white'}
                     }
                 
                 },
            ],
            'layout': 
            {
                #'title': new_title + " " + str(interval_value),
                'margin':dict(l=10, r=10, b=10, t=12),
                'autosize': True,
                "plot_bgcolor":"#444",
                "paper_bgcolor":"#444",
                #'font': {'color': "white"}
            },
            
        },
        config={
                'autosizable': True,
                'frameMargins': 0,
                'displaylogo': False,
                'editable': True
                },
        style={"width":"100%"})
        
    return content

def treemap(id_new, new_title, interval_value):
    content = dcc.Graph(
        id={"type": "graph", "index":id_new},
        figure={
            'data':
            [
                {'type': 'treemap',
                 'ids': ['a', 'b', 'c', 'd', 'e', 'f'],
                 'parents': ['', 'a', 'a', 'a', 'b', 'c'],
                 'labels': ['工廠 A', '機台1', '機台2', '機台3', 'EQNo', 'EQNo'],
                 #'colors': [1, 2, 2, 2, 3, 3],
                 'marker':{
                     'colors': [0.1, 0.2, 0.2, 0.2, 0.3, 0.3],
                     'colorscale': 'Portland',
                     }
                 }
            ],
            'layout': 
            {
                #'title': new_title + " " + str(interval_value),
                'margin':dict(l=10, r=20, b=10, t=30),
                'autosize': True,
                "plot_bgcolor":"#444",
                "paper_bgcolor":"#444",
            },
            
        },
        config={
                'autosizable': True,
                'frameMargins': 0,
                'displaylogo': False,
                },
        style={"width":"100%"})
        
    return content

def sunburst(id_new, new_title, interval_value):
    content = dcc.Graph(
        id={"type": "graph", "index":id_new},
        figure={
            'data':
            [
                {'type': 'sunburst',
                 'ids': ['a', 'b', 'c', 'd', 'e', 'f'],
                 'parents': ['', 'a', 'a', 'a', 'b', 'c'],
                 'labels': ['工廠 A', '機台1', '機台2', '機台3', 'EQNo', 'EQNo'],
                 #'colors': [1, 2, 2, 2, 3, 3],
                 'marker':{
                     'colors': [0.1, 0.2, 0.2, 0.2, 0.3, 0.3],
                     'colorscale': 'Greens',
                     }
                 }
            ],
            'layout': 
            {
                #'title': new_title + " " + str(interval_value),
                'margin':dict(l=10, r=20, b=10, t=15),
                'autosize': True,
                "plot_bgcolor":"#444",
                "paper_bgcolor":"#444",
            },
            
        },
        config={
                'autosizable': True,
                'frameMargins': 0,
                'displaylogo': False,
                },
        style={"width":"100%"})
        
    return content
