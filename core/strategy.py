from core.indicators import compute_rsi, compute_macd, detect_market_phase
from core.risk_manager import calculate_position_size

class TradingStrategy:
    def __init__(self, symbols):
        self.symbols = symbols

    def generate_signal(self, symbol, data):
        if not isinstance(data, pd.DataFrame) or len(data) < 15:
            return "HOLD"

        rsi = compute_rsi(data["close"].values)
        macd, _ = compute_macd(data["close"].values)
        phase = detect_market_phase(data)

        if phase == "BULL" and rsi > 70 and macd > 0:
            return "BUY"
        elif phase == "BEAR" and rsi < 30 and macd < 0:
            return "SELL"
        else:
            return "HOLD"
