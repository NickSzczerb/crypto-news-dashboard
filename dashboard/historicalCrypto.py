import json
import time
import os
import numpy as np
import pandas as pd
import investpy

def historicalData(coin, startTime, endTime):
    df2 = investpy.crypto.get_cryptos().head(20)
    coinName = df2.loc[df2['symbol'] == coin]['name'].values[0]
    # startTime: dd/mm/yyyy
    # endTime: dd/mm/yyyy
    search_result = investpy.crypto.get_crypto_historical_data(
        coinName, startTime, endTime)
    return search_result
