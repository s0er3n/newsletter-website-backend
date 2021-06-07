import yfinance as yf

def get_history(ticker: str):
    ticker = yf.Ticker(ticker)
    hist = ticker.history("Max")
    return hist.to_dict()