# 📈 MarketEdge — Trade Smarter. Invest Better.

<div align="center">

![MarketEdge](https://img.shields.io/badge/MarketEdge-Stock%20Dashboard-00e676?style=for-the-badge&logo=chartdotjs&logoColor=black)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?style=for-the-badge&logo=vercel)](https://project-3-8i3c.vercel.app/)

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-000000?style=flat-square&logo=vercel)](https://project-3-8i3c.vercel.app/)

**A real-time stock market dashboard with live NSE/BSE/NASDAQ data, interactive charts, SIP calculator, watchlist, portfolio tracker and more.**

### 🔗 [project-3-8i3c.vercel.app](https://project-3-8i3c.vercel.app/)

</div>

---

## ✨ Features

### 📡 Live Market Data
- Real-time **NIFTY 50, SENSEX, NASDAQ, DOW JONES, BANK NIFTY**
- Fetched from **Yahoo Finance API** — no API key needed
- Auto-refreshes every **60 seconds**
- Green/red color coding for gains and losses

### 📊 Dashboard
- Live **NIFTY 50 intraday chart** with 1D / 1W / 1M / 3M / 6M / 1Y / 5Y tabs
- **Top Gainers & Losers** — live sorted by % change
- **Market Overview** panel with 5 major indices + sparklines
- **Recent News** feed

### 🧮 SIP Calculator
- **SIP & Lumpsum** modes
- Interactive sliders for amount, return rate, time period
- Live **donut chart** — invested vs estimated returns
- **Year-by-Year growth bar chart**

### 📁 All Sections

| # | Section | What it shows |
|---|---|---|
| 1 | **Dashboard** | Live chart, gainers, losers, news |
| 2 | **Watchlist** | Personal stock tracker |
| 3 | **Markets** | Global indices + sector performance |
| 4 | **Analysis** | Sentiment, FII/DII, volume movers |
| 5 | **News** | Financial news by category |
| 6 | **Portfolio** | Holdings, P&L, % return |
| 7 | **Alerts** | Price alert management |
| 8 | **Calculator** | SIP & Lumpsum investment planner |
| 9 | **Reports** | Monthly P&L + trade summary |
| 10 | **Settings** | Preferences & display toggles |

### 📱 Mobile Responsive
- Hamburger ☰ menu — sidebar slides in from left
- Collapsing grids on small screens
- Works on all screen sizes from 380px and up

---

## 🗂️ Project Structure

```
MarketEdge/
├── index.html        # Landing page — hero, ticker, market cards
├── dashboard.html    # Main app — all 10 sections in one file
├── watchlist.html    # Standalone watchlist page
├── backend.py        # Python backend
├── styal.css         # Extra animations and mobile fixes
└── README.md         # This file
```

---

## 🚀 Getting Started

### Run Locally
```bash
# Clone the repo
git clone https://github.com/MohammedIsmail-SDE/Project-3.git
cd Project-3

# Open directly in browser — no build step needed
open index.html

# Or use a local dev server
python3 -m http.server 5500
# Visit: http://localhost:5500
```

### Deploy to Vercel
```bash
npm i -g vercel
vercel --prod
```

---

## 📡 Data Sources

| Data | Source | Cost |
|---|---|---|
| NIFTY / SENSEX | Yahoo Finance (`^NSEI`, `^BSESN`) | Free |
| NASDAQ / DOW JONES | Yahoo Finance (`^IXIC`, `^DJI`) | Free |
| Intraday chart | Yahoo Finance (5m intervals) | Free |

> Data fetched client-side via [corsproxy.io](https://corsproxy.io) — no API key required.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Charts | Chart.js + Custom SVG |
| Fonts | Google Fonts — Syne + DM Sans |
| Data | Yahoo Finance API |
| Hosting | Vercel |

---

## 👨‍💻 Author

**Mohammed Ismail**

[![GitHub](https://img.shields.io/badge/GitHub-MohammedIsmail--SDE-181717?style=flat-square&logo=github)](https://github.com/MohammedIsmail-SDE)

---

## 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ and lots of ☕

</div>