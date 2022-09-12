import dash_tvlwc
import dash
from dash.dependencies import Input, Output, State
from dash import html, dcc

from usage_dummy_data import candlestick_data, series_data

app = dash.Dash(__name__)

class Colors:
    backgroundType = 'solid'
    backgroundColor = '#1B2631'
    lineColor = '#2962FF'
    textColor = 'white'
    areaTopColor = '#2962FF'
    areaBottomColor = 'rgba(41, 98, 255, 0.28)'


chart_options = {
    'layout': {
        'background': {'type': Colors.backgroundType, 'color': Colors.backgroundColor},
        'textColor': Colors.textColor,
    },
    'grid': {
        'vertLines': {'visible': False},
        'horzLines': {'visible': False},
    },
    # 'width': 100,
    # 'height': 200
}

# seriesType options: https://tradingview.github.io/lightweight-charts/docs/api/interfaces/SeriesOptionsMap
data = [
    {
        'seriesData': candlestick_data,
        'seriesType': 'Candlestick',
        # 'seriesOptions': {'upColor': '#ffffff'}
    },
    {
        'seriesData': series_data,
        'seriesType': 'Area',
        # 'seriesOptions': {'lineWidth': 1}
    }
]

app.layout = html.Div([
    html.Div(children=[
        html.P(f'There are {len(candlestick_data)} datapoints. Show only recent:'),
        dcc.Input(id='input', type='number', value=len(candlestick_data)),
        html.Button('Submit', id='input-submit'),
    ]),
    
    html.Div(children=[
        html.P(f'Change background color'),
        dcc.Input(id='background-color', type='text', value='#1B2631'),
        html.Button('Submit', id='background-color-submit'),
    ]),
    
    html.Div(
        dash_tvlwc.Tvlwc(
            id='tv-chart',
            data=data,
            width='100%',
            height=400,
            chartOptions=chart_options
        ), style={'background': 'grey'}
    )
])


# @app.callback(
#     [Output('tv-chart', 'data')], 
#     [Input('input-submit', 'n_clicks')],
#     [State('input', 'value')]
# )
# def display_output(n, value):
#     return [candlestick_data[-value:]]


# @app.callback(
#     [Output('tv-chart', 'chartOptions')], 
#     [Input('background-color-submit', 'n_clicks')],
#     [State('background-color', 'value')]
# )
# def display_output(n, value):
#     chart_options = {
#         'layout': {
#             'background': {'type': Colors.backgroundType, 'color': value},
#             'textColor': Colors.textColor,
#         },
#         'grid': {
#             'vertLines': {'visible': False},
#             'horzLines': {'visible': False},
#         },
#     }
#     return [chart_options]



if __name__ == '__main__':
    app.run_server(debug=True)
