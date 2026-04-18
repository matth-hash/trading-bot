import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
FRED_API_KEY = os.getenv("FRED_API_KEY")

# Webhook URL
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Trading Config
MIN_SCORE = 75
MAX_TRADES_PER_SCAN = 3
SL_PCT = 0.02  # Stop-loss à 2%
TP_PCT = 0.05  # Take-profit à 5%
SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "ADAUSDT", "DOTUSDT"]
