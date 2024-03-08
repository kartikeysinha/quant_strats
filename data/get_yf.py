"""
Purpose: Retrieve common data from Yahoo Finance
"""

import pandas as pd
import numpy as np
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
    # TODO: Error handling

    return df


def get_returns_from_candles(
    df_candles : pd.DataFrame,
    candle_info_to_use : str = "Adj Close"
) -> pd.DataFrame:
    """
    Calcualate the log returns from the candles provided.

    Args
    ----
    df_candles : candles dataframe
    candle_info_to_use : specifying which candle information to use to get returns.
    """
    
    return np.log( df_candles[candle_info_to_use] / df_candles[candle_info_to_use].shift(1) )


