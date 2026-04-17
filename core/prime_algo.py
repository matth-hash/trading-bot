from core.data_collector import get_market_data
from core.macro_filter import get_macro_bias
from core.ml_model import compute_score
from core.strategy import TradingStrategy

def run_scan():
    market_data = get_market_data()
    macro = get_macro_bias()
    strategy = TradingStrategy(market_data.keys())
    results = []

    for symbol, data in market_data.items():
        if data.empty or len(data) < 15:
            continue  # Passe à la paire suivante si les données sont insuffisantes

        signal = strategy.generate_signal(symbol, data)
        score = compute_score(data, macro)
        if signal != "HOLD" and score > 75:
            results.append({
                "symbol": symbol,
                "signal": signal,
                "score": score
            })

    return results
