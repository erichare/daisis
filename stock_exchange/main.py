import yfinance as yf
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.embed import file_html
from bokeh.resources import Resources
import datetime
from datetime import date
from datetime import timedelta
import numpy as np
import base64

color_list = ["blue" , "red", "green", "orange", "purple", "yellow"]


def plot_correlation(Symbol1, Symbol2, period):
    title = 'Normalised correlation between ' + str(Symbol1) + ' and ' + str(Symbol2)

    p = figure(title=title, x_axis_label="Date", y_axis_label="Opening Price",
               x_axis_type='datetime', sizing_mode='stretch_both')
    today = date.today()

    tickerSymbol = [str(Symbol1), str(Symbol2)]

    full_tickerDf = pd.DataFrame()
    i = 0
    for t in tickerSymbol:
        tickerData = yf.Ticker(t)

        tickerDf = tickerData.history(period='1d', start=today - timedelta(days = int(period)), end=today)
        tickerDf['Open'] /= np.max(tickerDf['Open'])
        tickerDf["Symbol"] = t
        tickerDf["Date"] = tickerDf.index

        p.line(tickerDf["Date"].tolist(), tickerDf["Open"].tolist(),
        legend_label=t, line_color=color_list[i % len(color_list)], line_width=2)

        full_tickerDf = pd.concat([full_tickerDf, tickerDf], ignore_index=True)

        i += 1

    return p, full_tickerDf


def compute(Symbol1, Symbol2, period):

    p, df = plot_correlation(Symbol1, Symbol2, period)

    html_out = file_html(p, Resources('inline', minified=True))

    return [{"type": "html", "data": html_out},
            {"type": "dataframe", "id": "dataframe", "label": "Stock History", "data": df}]

def schema():
    r = [
            {
                "id": "Symbol1",
                "type": "text",
                "label": "First Symbol to Plot",
                "initialValue": "AAPL",
                "props": {
                    "type": 'text'
                }
            },
            {
                "id": "Symbol2",
                "type": "text",
                "label": "Second Symbol to Plot",
                "initialValue": "GOOG",
                "props": {
                    "type": 'text'
                }
            },
            {
                "id": "period",
                "type": "text",
                "label": "Correlation will be shown for x days before today",
                "initialValue": 365,
                "props": {
                    "type": 'number'
                }
            },

    ]

    return r
