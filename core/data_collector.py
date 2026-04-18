import requests
import pandas as pd
from core.config import SYMBOLS

# Binance API
BINANCE_BASE_URL = "https://api.binance.com/api/v3/klines"
# Bybit API (endpoint public)
BYBIT_BASE_URL = "https://api.bybit.com/v2/public/kline/list"
# MEXC API (endpoint public)
MEXC_BASE_URL = "https://www.mexc.com/api/v3/klines"

def get_klines_binance(symbol, interval="1m", limit=100):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    try:
        response = requests.get(BINANCE_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Erreur lors de la récupération des données Binance pour {symbol}: {e}")
        return pd.DataFrame(columns=["time", "close"])

    columns = ["time", "open", "high", "low", "close", "volume", "close_time",
               "quote_asset_volume", "number_of_trades", "taker_buy_base", "taker_buy_quote", "ignore"]
    df = pd.DataFrame(data, columns=columns)

    if df.empty:
        return df

    df["time"] = pd.to_datetime(df["time"], unit="ms", errors='coerce')
    df["close"] = pd.to_numeric(df["close"], errors='coerce')

    return df.dropna(subset=["close"])

def get_klines_bybit(symbol, interval="1", limit=100):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    try:
        response = requests.get(BYBIT_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()["result"]
    except Exception as e:
        print(f"Erreur lors de la récupération des données Bybit pour {symbol}: {e}")
        return pd.DataFrame(columns=["time", "close"])

    columns = ["time", "open", "high", "low", "close", "volume"]
    df = pd.DataFrame(data, columns=columns)

    if df.empty:
        return df

    df["time"] = pd.to_datetime(df["time"], unit="ms", errors='coerce')
    df["close"] = pd.to_numeric(df["close"], errors='coerce')

    return df.dropna(subset=["close"])

def get_klines_mexc(symbol, interval="1m", limit=100):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }
    try:
        response = requests.get(MEXC_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Erreur lors de la récupération des données MEXC pour {symbol}: {e}")
        return pd.DataFrame(columns=["time", "close"])

    columns = ["time", "open", "high", "low", "close", "volume", "close_time",
               "quote_asset_volume", "number_of_trades", "taker_buy_base", "taker_buy_quote", "ignore"]
    df = pd.DataFrame(data, columns=columns)

    if df.empty:
        return df

    df["time"] = pd.to_datetime(df["time"], unit="ms", errors='coerce')
    df["close"] = pd.to_numeric(df["close"], errors='coerce')

    return df.dropna(subset=["close"])

def get_market_data():
    market_data = {}
    for symbol in SYMBOLS:
        # Récupère les données depuis Binance
        binance_data = get_klines_binance(symbol)
        # Récupère les données depuis Bybit
        bybit_data = get_klines_bybit(symbol)
        # Récupère les données depuis MEXC
        mexc_data = get_klines_mexc(symbol)

        # Logs pour suivre la source utilisée
        print(f"Données récupérées pour {symbol}: Binance={len(binance_data)}, Bybit={len(bybit_data)}, MEXC={len(mexc_data)}")

        # Logique de croisement des données
        if not binance_data.empty and len(binance_data) >= 15:
            print(f"Utilisation des données Binance pour {symbol}.")
            market_data[symbol] = binance_data
        elif not bybit_data.empty and len(bybit_data) >= 15:
            print(f"Utilisation des données Bybit pour {symbol}.")
            market_data[symbol] = bybit_data
        elif not mexc_data.empty and len(mexc_data) >= 15:
            print(f"Utilisation des données MEXC pour {symbol}.")
            market_data[symbol] = mexc_data
        else:
            print(f"Aucune source de données valide pour {symbol}.")
            market_data[symbol] = pd.DataFrame(columns=["time", "close"])

    return market_data
