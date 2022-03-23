import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objs as go
import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
from historicalCrypto import historicalData
from charts import candle_chart, moving_average
import yfinance as yfB


# -----------Page Layout----------------------

st.set_page_config(layout="wide")
st.title("Crypto News Tracker")

# -----------Date Input------------------------

st.sidebar.write("Please choose the crypto and dates:")

today = dt.datetime.today()

start = st.sidebar.date_input('Start date:',
                                   today - dt.timedelta(days=90*3),
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
period = 0
if ma_flag:
    period = st.sidebar.slider("Choose Period", min_value=7, max_value=100)
st.text("")


# ------------Plot Functions-------------------




df = yfB.download(f'{ticker_name}-USD', start,
                  end).drop(columns='Adj Close').reset_index()
#historicalData(ticker_name, start.strftime('%d/%m/%Y'),end.strftime('%d/%m/%Y')).reset_index()

st.plotly_chart(candle_chart(df, ticker_name, start, end, period, ma=ma_flag),
                use_container_width=True)

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
