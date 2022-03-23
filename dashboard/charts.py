import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objs as go
import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
from historicalCrypto import historicalData


def moving_average(data, column, period, new_columns_only=False):
    """Average price over a specified period.
       Input:
           data: dataframe.
           column: column name to apply the moving avreage.
           period: number of days of the window.
           new_columns_only: True to return only the moving average column.
                             False to return the original dataframe with the new moving average column.
       Output: a dataframe with the {column}_ma{period}"""
    new_column_name = f'{column}_ma{int(period)}'
    result = data.copy()
    result[new_column_name] = result[column].rolling(window=period,
                                                     closed='right').mean()
    if new_columns_only:
        return result[[new_column_name]]
    return result

def candle_chart(df, ticker_name, start, end, period=1,ma=False):
    fig = go.Figure(data=[
        go.Candlestick(name=f"Candlestick",
                       x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])
    ])
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        title=f'Chart containing {ticker_name} prices from {start} to {end}',
        yaxis_title=f'{ticker_name}',
        shapes=[
            dict(x0=start,
                x1=end,
                y0=0,
                y1=1,
                xref='x',
                yref='paper',
                line_width=2)
        ])
    if ma:
        ma_data = moving_average(df,'Close',period)
        fig.add_trace(
            go.Scatter(
            x=ma_data["Date"],
            y=ma_data[f"Close_ma{int(period)}"],
            mode="markers+lines",
            name=f"{period} Day Moving Average",
            line=dict(
                color="blue")))
    return fig
