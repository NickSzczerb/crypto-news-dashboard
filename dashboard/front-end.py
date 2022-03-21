import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objs as go
import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
import requests

# -----------Page Layout----------------------

st.set_page_config(layout="wide")
st.title("Crypto News Tracker")

# -----------Date Input------------------------

st.sidebar.write("Please choose the crypto and dates:")

today = dt.datetime.today()

start = st.sidebar.date_input('Start date:',
                                   today - dt.timedelta(days=90*1),
                                   min_value=today - dt.timedelta(days=365*10),
                                   max_value=today - dt.timedelta(days=31*2))
end = st.sidebar.date_input('End date:',
                                 min_value=start +
                                 dt.timedelta(days=31*2),
                                 max_value=today)

# -----------Stock Selection-------------------

selected_crypto = ("BTC", "ETH", "CRO","BNB")
ticker_name = st.sidebar.selectbox("Select Crypto:", selected_crypto)

# ---------------Load Data---------------------


# -----------Company Name-------------------




#---------------Recommendations section--------------





# ----------Indicator Selection----------------

st.text("")
ma_flag = st.sidebar.checkbox("Moving Average", value=False)
if ma_flag:
    period = st.sidebar.slider("Choose Period", min_value=7, max_value=100)
st.text("")


# ------------Plot Functions-------------------




st.markdown(f"""
            ## You are looking at   {ticker_name} data

            #### Change your crypto with the menu on the left """
            )

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
)
fig = go.Figure(data=[
    go.Candlestick(x=df['Date'],
                   open=df['AAPL.Open'],
                   high=df['AAPL.High'],
                   low=df['AAPL.Low'],
                   close=df['AAPL.Close'])
])
fig.update_layout(title='Example of Candlestick Chart',
                  yaxis_title='AAPL Stock',
                  shapes=[
                      dict(x0='2016-12-09',
                           x1='2016-12-09',
                           y0=0,
                           y1=1,
                           xref='x',
                           yref='paper',
                           line_width=2)
                  ],
                  annotations=[
                      dict(x='2016-12-09',
                           y=0.05,
                           xref='x',
                           yref='paper',
                           showarrow=False,
                           xanchor='left',
                           text='Increase Period Begins')
                  ])
st.plotly_chart(fig,use_container_width=True)

st.markdown(""" Example of Data format required for chart """)
st.table(df.head(5))

st.markdown(f"""
            # Other Ideas

            #### twitter sentiment
            #### reddit sentiment
            #### greed index
            #### predictions for next X days
            #### buy vs sell
            """)
