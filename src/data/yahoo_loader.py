import yfinance as yf
import pandas as pd

def load_yahoo_data(ticker="RELIANCE.NS", start="2020-01-01", end="2024-01-01"):
    df = yf.download(ticker, start=start, end=end)

    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)

    return df