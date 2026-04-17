import requests
from core.config import FRED_API_KEY

def get_macro_bias():
    try:
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=DFF&api_key={FRED_API_KEY}&file_type=json"
        response = requests.get(url)
        data = response.json()
        last_value = float(data["observations"][-1]["value"])

        if last_value > 2.5:
            return "BEARISH"
        elif last_value < 1.5:
            return "BULLISH"
        else:
            return "NEUTRAL"
    except Exception as e:
        print(f"Erreur lors de la récupération des données macro: {e}")
        return "NEUTRAL"
