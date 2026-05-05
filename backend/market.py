# #MarketEdge/
# │
# ├── frontend/
# │   └── index.html  ← your existing site
# │
# ├── backend/
# │   ├── main.py        ← FastAPI app
# │   ├── database.py    ← Portfolio DB
# │   └── market.py      ← Market data logic
import yfinance as yf

def get_stock_price(symbol: str):
    ticker = yf.Ticker(symbol)
    info = ticker.fast_info
    return {
        "symbol": symbol,
        "price": info.last_price,
        "change_percent": round(info.last_price / info.previous_close * 100 - 100, 2)
    }