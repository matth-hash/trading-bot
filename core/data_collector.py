import requests
import pandas as pd
from core.config import SYMBOLS, BINANCE_API_KEY, BINANCE_API_SECRET

BASE_URL = "https://api.binance.com/api/v3/klines"

def get_klines(symbol, interval="1m", limit=50):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    columns = ["time", "open", "high", "low", "close", "volume", "close_time",
               "quote_asset_volume", "number_of_trades", "taker_buy_base", "taker_buy_quote", "ignore"]
    df = pd.DataFrame(data, columns=columns)
    df["time"] = pd.to_datetime(df["time"], unit="ms")
    df["close"] = df["close"].astype(float)

    return df

def get_market_data():
    market_data = {}
    for symbol in SYMBOLS:
        market_data[symbol] = get_klines(symbol)
    return market_data
