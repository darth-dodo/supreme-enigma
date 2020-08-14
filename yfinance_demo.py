import yfinance as yf
from pprint import pprint

symbols = ["MSFT", "GOOG", "AAPL", "FB", "PG"]

for sym in symbols:
    print("====================")
    print(sym)
    data = yf.Ticker(sym)
    pprint(data.info)
    print("====================")
