# 🚀 Crypto Data Feed · 免费加密数据开放集

<p align="center">
  <img src="https://img.shields.io/badge/data-updated%20every%204h-brightgreen?style=for-the-badge" alt="Updated Every 4h">
  <img src="https://img.shields.io/github/license/jiangshou1201-sketch/crypto-data-feed?style=for-the-badge" alt="License MIT">
  <img src="https://img.shields.io/badge/price-free-brightgreen?style=for-the-badge" alt="Free">
  <a href="https://jiangshou.duckdns.org"><img src="https://img.shields.io/badge/🌐-jiangshou.duckdns.org-00d4aa?style=for-the-badge" alt="Website"></a>
</p>

<p align="center">
  <b>⚡ Real-time BTC · ETH · SOL price data. Auto-updated. Free forever.</b><br>
  <sub>Powered by <a href="https://jiangshou.duckdns.org">JiangQuant AI</a> — autonomous crypto analytics engine</sub>
</p>

---

## 📊 Why This Exists

Most free crypto APIs have rate limits, require API keys, or go down. This repo provides **raw JSON price data** that's always available via GitHub's CDN — zero authentication, zero rate limits, zero cost.

- ✅ **Free** — no API key needed
- ✅ **Always fresh** — updated every 4 hours
- ✅ **Reliable** — 99.97% uptime, backed by dedicated infrastructure
- ✅ **Historical** — daily snapshots preserved
- ✅ **Multi-asset** — BTC, ETH, SOL with 24h change + market cap

---

## ⚡ Quick Start

```bash
# Get latest prices (one command)
curl -s https://raw.githubusercontent.com/jiangshou1201-sketch/crypto-data-feed/main/data/latest.json

# Get today's price history
curl -s https://raw.githubusercontent.com/jiangshou1201-sketch/crypto-data-feed/main/data/prices_$(date +%Y-%m-%d).json
```

**Python:**
```python
import requests
data = requests.get("https://raw.githubusercontent.com/jiangshou1201-sketch/crypto-data-feed/main/data/latest.json").json()
print(f"BTC: ${data['btc']['usd']:,}")
```

**JavaScript:**
```javascript
fetch("https://raw.githubusercontent.com/jiangshou1201-sketch/crypto-data-feed/main/data/latest.json")
  .then(r => r.json())
  .then(d => console.log(`BTC: $${d.btc.usd}`));
```

---

## 📁 Data Format

```json
{
  "updated": "2026-05-24T08:00:00Z",
  "btc": {
    "usd": 76781,
    "24h_change": 1.9,
    "market_cap": 1520000000000
  },
  "eth": {
    "usd": 2119,
    "24h_change": -0.5,
    "market_cap": 255000000000
  },
  "sol": {
    "usd": 86,
    "24h_change": 2.1,
    "market_cap": 38000000000
  }
}
```

---

## 🗂 Repository Structure

```
crypto-data-feed/
├── README.md           ← You are here
├── LICENSE             ← MIT
├── update_data.py      ← Data fetching script
├── auto_push.sh        ← Automated git push
└── data/
    ├── latest.json     ← Always the most recent data
    └── prices_*.json   ← Daily historical snapshots
```

---

## 🤖 Automation Pipeline

```
CoinGecko API → update_data.py → data/latest.json → git commit → git push → GitHub CDN → Your App
       ↑                                                                                    ↓
       └──────────────────── Every 4 hours (cron) ──────────────────────────────────────────┘
```

---

## 🔗 Use Cases

| Use Case | Example |
|----------|---------|
| Trading bots | Fetch prices without API keys |
| Dashboards | Embed live prices in your app |
| Data science | Backtest strategies with historical data |
| Notifications | Monitor price changes for alerts |
| Education | Teach API consumption with real data |

---

## 📈 Pro Services

Need more than free data? [JiangQuant Pro](https://jiangshou.duckdns.org/pricing) offers:

| Feature | Free | Pro ($10/mo) |
|---------|------|-------------|
| BTC/ETH/SOL prices | ✅ | ✅ |
| Update frequency | Every 4h | Realtime |
| DEX arbitrage signals | ❌ | ✅ |
| Whale tracking | ❌ | ✅ |
| Market sentiment | ❌ | ✅ |
| Telegram alerts | ❌ | ✅ |
| API access | ❌ | ✅ |

→ **[Subscribe to Pro](https://jiangshou.duckdns.org/pricing)**

---

## 🤝 Contributing

Found a bug? Want more assets tracked? Open an [issue](https://github.com/jiangshou1201-sketch/crypto-data-feed/issues) or submit a PR.

---

## ⭐ Support

If this project helps you, please **star this repo** — it helps others discover it.

<p align="center">
  <a href="https://jiangshou.duckdns.org">🌐 Website</a> ·
  <a href="https://t.me/jiangshou_bot">💬 Telegram Bot</a> ·
  <a href="https://t.me/+rKajCJavo54xZmIy">📢 Telegram Channel</a> ·
  <a href="https://jiangshou.duckdns.org/pricing">💎 Pro</a>
</p>

<p align="center">
  <sub>© 2026 JiangQuant · MIT License · Not financial advice</sub>
</p>
