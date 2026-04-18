import requests
import pandas as pd
from core.config import SYMBOLS

def get_coingecko_data(symbol, vs_currency="usd", days="1"):
    coin_id = symbol.split('USDT')[0].lower()
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        'vs_currency': vs_currency,
        'days': days
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données CoinGecko pour {symbol}: {e}")
        return pd.DataFrame(columns=["time", "close"])

    prices = data['prices']
    df = pd.DataFrame(prices, columns=["time", "close"])
    df["time"] = pd.to_datetime(df["time"], unit="ms", errors='coerce')
    return df.dropna(subset=["close"])

def get_market_data():
    market_data = {}
    for symbol in SYMBOLS:
        data = get_coingecko_data(symbol)
        if not data.empty:
            market_data[symbol] = data
        else:
            print(f"Aucune source de données valide pour {symbol}.")
            market_data[symbol] = pd.DataFrame(columns=["time", "close"])

    return market_data
