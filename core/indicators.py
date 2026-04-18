import pandas as pd
import numpy as np

def compute_rsi(closes, period=14):
    if not isinstance(closes, (np.ndarray, list, pd.Series)) or len(closes) < period + 1:
        return 50  # Retourne une valeur par défaut si les données sont insuffisantes

    try:
        deltas = np.diff(closes)
        seed = deltas[:period+1]
        up = seed[seed >= 0].sum() / period
        down = -seed[seed < 0].sum() / period
        rs = up / down if down != 0 else 1
        rsi = np.zeros_like(closes)
        rsi[:period] = 100. - 100. / (1. + rs)

        for i in range(period, len(closes)):
            delta = deltas[i-1]
            if delta > 0:
                upval = delta
                downval = 0.
            else:
                upval = 0.
                downval = -delta

            up = (up * (period - 1) + upval) / period
            down = (down * (period - 1) + downval) / period
            rs = up / down if down != 0 else 1
            rsi[i] = 100. - 100. / (1. + rs)

        return rsi[-1] if len(rsi) > 0 else 50
    except Exception as e:
        print(f"Erreur dans compute_rsi: {e}")
        return 50

def compute_macd(closes, slow=26, fast=12, signal=9):
    if not isinstance(closes, (np.ndarray, list, pd.Series)) or len(closes) < max(slow, fast, signal):
        return 0, 0  # Retourne des valeurs par défaut si les données sont insuffisantes

    try:
        ema_fast = pd.Series(closes).ewm(span=fast, adjust=False).mean()
        ema_slow = pd.Series(closes).ewm(span=slow, adjust=False).mean()
        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal, adjust=False).mean()

        return macd.iloc[-1] if len(macd) > 0 else 0, signal_line.iloc[-1] if len(signal_line) > 0 else 0
    except Exception as e:
        print(f"Erreur dans compute_macd: {e}")
        return 0, 0

def detect_market_phase(data):
    if not isinstance(data, pd.DataFrame) or len(data) < 15:
        return "NEUTRAL"

    try:
        closes = data["close"].values
        rsi = compute_rsi(closes)
        macd, _ = compute_macd(closes)

        if rsi > 70 and macd > 0:
            return "BULL"
        elif rsi < 30 and macd < 0:
            return "BEAR"
        else:
            return "NEUTRAL"
    except Exception as e:
        print(f"Erreur dans detect_market_phase: {e}")
        return "NEUTRAL"
