from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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