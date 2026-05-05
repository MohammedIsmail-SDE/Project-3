import sqlite3

def init_db():
    conn = sqlite3.connect("portfolio.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS holdings (
            id INTEGER PRIMARY KEY,
            symbol TEXT,
            quantity REAL,
            buy_price REAL
        )
    """)
    conn.commit()
    conn.close()

def add_holding(symbol, quantity, buy_price):
    init_db()
    conn = sqlite3.connect("portfolio.db")
    conn.execute("INSERT INTO holdings VALUES (NULL,?,?,?)", (symbol, quantity, buy_price))
    conn.commit()
    conn.close()

def get_portfolio():
    init_db()
    conn = sqlite3.connect("portfolio.db")
    rows = conn.execute("SELECT symbol, quantity, buy_price FROM holdings").fetchall()
    conn.close()
    return [{"symbol": r[0], "quantity": r[1], "buy_price": r[2]} for r in rows]