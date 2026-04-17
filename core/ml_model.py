def compute_score(data, macro):
    score = 0

    # Volatility
    volatility = data["close"].pct_change().std()
    if volatility > 0.01:
        score += 20

    # Trend
    trend = data["close"].iloc[-1] - data["close"].iloc[-10]
    if trend > 0:
        score += 20

    # Macro bias
    if macro == "BULLISH":
        score += 30
    elif macro == "BEARISH":
        score -= 10

    return min(score, 100)
