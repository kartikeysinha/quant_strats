"""
Purpose: Retrieve common data from Yahoo Finance
"""

import pandas as pd
import yfinance as yf
import datetime as dt

def get_candles(
    tickers : list[str],
    start_date : str = "2010-01-01",
    end_date : str = dt.datetime.now().strftime("%Y-%m-%d"),
    freq : str = '1d'
) -> pd.DataFrame:
    """
    Get candle information for the requested tickers, desired date range, and the desired freqeuncy.
    """
    
    df = yf.download(tickers=tickers, start=start_date, end=end_date, interval=freq)

    return df
