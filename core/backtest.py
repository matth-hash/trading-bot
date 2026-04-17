from core.market_data import get_klines
from core.strategy import TradingStrategy

def run_backtest(symbol="BTCUSDT", start_date=None, end_date=None):
    data = get_klines(symbol, limit=1000)  # Récupère 1000 bougies
    strategy = TradingStrategy([symbol])

    trades = []
    for i in range(50, len(data)):
        signal = strategy.generate_signal(symbol, data.iloc[:i])
        if signal != "HOLD":
            trades.append({
                "symbol": symbol,
                "signal": signal,
                "price": data.iloc[i]["close"],
                "time": data.iloc[i]["time"]
            })

    return trades
