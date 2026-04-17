import pandas as pd
import numpy as np

def compute_rsi(closes, period=14):
    deltas = np.diff(closes)
    seed = deltas[:period+1]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down
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
        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)

    return rsi

def compute_macd(closes, slow=26, fast=12, signal=9):
    ema_fast = pd.Series(closes).ewm(span=fast, adjust=False).mean()
    ema_slow = pd.Series(closes).ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def detect_market_phase(data):
    closes = data["close"].values
    rsi = compute_rsi(closes)
    macd, _ = compute_macd(closes)

    # Accéder à la dernière valeur de la série pandas
    last_macd = macd.iloc[-1]

    if rsi[-1] > 70 and last_macd > 0:
        return "BULL"
    elif rsi[-1] < 30 and last_macd < 0:
        return "BEAR"
    else:
        return "NEUTRAL"
