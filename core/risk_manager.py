from core.config import SL_PCT, TP_PCT

def calculate_position_size(account_balance, risk_per_trade=0.01):
    return account_balance * risk_per_trade

def calculate_stop_loss(entry_price):
    return entry_price * (1 - SL_PCT)

def calculate_take_profit(entry_price):
    return entry_price * (1 + TP_PCT)
