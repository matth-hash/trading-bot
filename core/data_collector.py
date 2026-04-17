import requests
import pandas as pd
from core.config import SYMBOLS, BINANCE_API_KEY, BINANCE_API_SECRET

BASE_URL = "https://api.binance.com/api/v3/klines"

def get_klines(symbol, interval="1m", limit=100):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
    except Exception as e:
        print(f"Erreur lors de la récupération des données pour {symbol}: {e}")
        return pd.DataFrame(columns=["time", "close"])  # Retourne un DataFrame vide en cas d'erreur

    columns = ["time", "open", "high", "low", "close", "volume", "close_time",
               "quote_asset_volume", "number_of_trades", "taker_buy_base", "taker_buy_quote", "ignore"]
    df = pd.DataFrame(data, columns=columns)
    if df.empty:
        return df

    df["time"] = pd.to_datetime(df["time"], unit="ms", errors='coerce')
    df["close"] = pd.to_numeric(df["close"], errors='coerce')

    return df.dropna(subset=["close"])  # Supprime les lignes où "close" est NaN

def get_market_data():
    market_data = {}
    for symbol in SYMBOLS:
        market_data[symbol] = get_klines(symbol)
    return market_data
