try:
    from fastapi import FastAPI  # type: ignore[reportMissingImports]
    from fastapi.middleware.cors import CORSMiddleware  # type: ignore[reportMissingImports]
except ImportError:
    class FastAPI:
        def __init__(self, *args, **kwargs):
            pass

        def add_middleware(self, *args, **kwargs):
            pass

        def get(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

        def post(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

    class CORSMiddleware:
        pass

from market import get_stock_price
from database import add_holding, get_portfolio

app = FastAPI()

# Allow your HTML frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Real-time market data
@app.get("/price/{symbol}")
def stock_price(symbol: str):
    return get_stock_price(symbol)

# Portfolio routes
@app.post("/portfolio/add")
def add_stock(symbol: str, quantity: float, buy_price: float):
    add_holding(symbol, quantity, buy_price)
    return {"message": "Added successfully"}

@app.get("/portfolio")
def portfolio():
    return get_portfolio()