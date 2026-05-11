# #MarketEdge/
# │
# ├── frontend/
# │   └── index.html  ← your existing site
# │
# ├── backend/
# │   ├── main.py        ← FastAPI app
# │   ├── database.py    ← Portfolio DB
# │   └── market.py      ← Market data logic
import json
import urllib.request

def get_stock_price(symbol: str):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
    with urllib.request.urlopen(url) as response:
        data = json.load(response)

    result = data.get("quoteResponse", {}).get("result", [])
    if not result:
        raise ValueError(f"No data for symbol {symbol}")

    quote = result[0]
    price = quote.get("regularMarketPrice")
    previous_close = quote.get("regularMarketPreviousClose")
    if price is None or previous_close is None:
        raise ValueError(f"Incomplete market data for symbol {symbol}")

    return {
        "symbol": symbol,
        "price": price,
        "change_percent": round(price / previous_close * 100 - 100, 2)
    }