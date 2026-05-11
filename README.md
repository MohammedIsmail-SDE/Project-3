# 📈 MarketEdge — Stock Market Dashboard

<div align="center">

![MarketEdge Banner](https://img.shields.io/badge/MarketEdge-Stock%20Dashboard-00e676?style=for-the-badge&logo=chartdotjs&logoColor=black)

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**A real-time stock market dashboard with live NSE/BSE/NASDAQ data, interactive charts, SIP calculator, and personal watchlist.**

[🚀 Live Demo](#) · [📸 Screenshots](#screenshots) · [⚙️ Features](#features) · [🛠️ Setup](#setup)

</div>

---

## 📸 Screenshots

### 🏠 Landing Page
> Dark-themed hero with live market ticker, candlestick chart, and Nifty/Sensex/NASDAQ cards

### 📊 Dashboard
> Real-time NIFTY 50 chart, market overview, top gainers/losers, and live news

### 📋 Watchlist
> Personal stock watchlist with live prices, sparkline trends, and add/remove functionality

### 🧮 SIP Calculator
> Systematic Investment Plan calculator with interactive donut chart and year-by-year growth bar chart

---

## ✨ Features

### 📡 Real-Time Market Data
- Live prices for **NIFTY 50, SENSEX, NASDAQ, DOW JONES, BANK NIFTY**
- Data fetched directly from **Yahoo Finance API** (no API key required)
- Auto-refresh every **60 seconds**
- Color-coded **green/red** for gainers and losers

### 📊 Interactive Dashboard
- **Live intraday chart** for NIFTY 50 with real 5-minute candle data
- **Time range tabs** — 1D, 1W, 1M, 3M, 6M, 1Y, 5Y
- **Top Gainers & Losers** table — auto-sorted by % change
- **Market Overview** panel with 5 major indices
- **Recent News** section

### 📋 Watchlist
- **Add/Remove** stocks from a personal watchlist
- **Live prices** with sparkline trend charts
- **52-Week High/Low** for each stock
- **Filter** by All / Gainers / Losers
- **Sort** by name, price, change, % change
- **Persistent storage** — saved in localStorage across sessions
- **Price Alert** button for each stock

### 🧮 SIP Calculator
- **SIP & Lumpsum** modes with toggle
- Interactive **sliders** for investment amount, return rate, time period
- **Donut chart** showing invested vs estimated returns
- **Year-by-year bar chart** showing growth over time
- Real-time calculation as sliders move

### 🎨 UI/UX
- **Dark theme** inspired by Bloomberg & TradingView
- **Smooth animations** and hover effects throughout
- **Responsive** design for all screen sizes
- **Google Fonts** — Syne + DM Sans
- **Live ticker tape** scrolling across the top

---

## 🗂️ Project Structure

```
MarketEdge/
│
├── 📄 index.html          # Landing page with hero section
├── 📄 dashboard.html      # Main dashboard + SIP Calculator
├── 📄 watchlist.html      # Personal watchlist page
├── 📄 styal.css           # Global animation styles
│
└── 📁 backend/
    ├── 🐍 main.py         # Flask server entry point
    ├── 🐍 database.py     # Database models & operations
    ├── 🐍 market.py       # Market data fetching logic
    └── 🐍 backend.py      # API routes & business logic
```

---

## 🛠️ Setup

### Frontend (No setup needed!)
Just open `index.html` in your browser — it works instantly.

```bash
# Clone the repo
git clone https://github.com/MohammedIsmail-SDE/Project-3.git

# Open in browser
open index.html
# or simply double-click index.html
```

### Backend (Python Flask)

```bash
# Navigate to backend folder
cd backend

# Install dependencies
pip install flask flask-cors yfinance

# Run the server
python main.py
```

Server runs on `http://localhost:5000`

---

## 🔗 How Pages Connect

```
index.html  ──[Explore Markets]──▶  dashboard.html
                                         │
                              ┌──────────┴──────────┐
                              │                     │
                        [Watchlist]           [Calculator]
                              │
                        watchlist.html
```

---

## 📡 Data Sources

| Data | Source | Cost |
|------|--------|------|
| Stock prices | Yahoo Finance API | Free |
| NIFTY / SENSEX | Yahoo Finance (`^NSEI`, `^BSESN`) | Free |
| NASDAQ / DOW | Yahoo Finance (`^IXIC`, `^DJI`) | Free |
| Intraday charts | Yahoo Finance (5m intervals) | Free |

> All data is fetched client-side via [corsproxy.io](https://corsproxy.io) — no API key required.

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Charts | SVG (custom), Chart.js |
| Fonts | Google Fonts (Syne, DM Sans) |
| Backend | Python, Flask, Flask-CORS |
| Data | Yahoo Finance API (yfinance) |
| Storage | localStorage (watchlist persistence) |

---

## 🚀 Pages Overview

### `index.html` — Landing Page
- Animated hero with **"Trade Smarter. Invest Better."**
- Live scrolling ticker tape
- NIFTY 50, SENSEX, NASDAQ live cards with sparklines
- Candlestick chart visualization
- Feature highlights section
- **"Explore Markets"** button → navigates to dashboard

### `dashboard.html` — Main Dashboard
- Sidebar navigation with **10 menu items**
- Live NIFTY 50 area chart (real intraday data)
- Market Overview with 5 indices
- Top Gainers & Top Losers tables (live data)
- Recent News section
- Built-in **SIP Calculator** (accessible from sidebar)

### `watchlist.html` — Watchlist
- Personal stock watchlist (20 NSE stocks available)
- Stats bar: Total stocks, Gainers, Losers, Top Gainer
- Filter + Search + Sort functionality
- Add/Remove stocks with confirmation toast
- Sparkline mini charts per stock

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Mohammed Ismail**

[![GitHub](https://img.shields.io/badge/GitHub-MohammedIsmail--SDE-181717?style=flat-square&logo=github)](https://github.com/MohammedIsmail-SDE)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ and lots of ☕

</div>
