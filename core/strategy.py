from core.indicators import compute_rsi, compute_macd, detect_market_phase
from core.risk_manager import calculate_position_size

class TradingStrategy:
    def __init__(self, symbols):
        self.symbols = symbols

    def generate_signal(self, symbol, data):
    if len(data) < 15:  # Vérifie qu'il y a assez de données
        return "HOLD"

    rsi = compute_rsi(data["close"].values)
    macd, _ = compute_macd(data["close"].values)
    phase = detect_market_phase(data)

    if phase == "BULL" and rsi[-1] > 70 and macd.iloc[-1] > 0:
        return "BUY"
    elif phase == "BEAR" and rsi[-1] < 30 and macd.iloc[-1] < 0:
        return "SELL"
    else:
        return "HOLD"
