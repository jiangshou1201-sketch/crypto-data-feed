# Crypto Data Feed · 加密数据开放集

> **Free, Auto-Updated Crypto Price Data** — BTC · ETH · SOL  
> Powered by [JiangQuant AI](https://jiangshou.duckdns.org) · 24/7 Automated

[![Updated](https://img.shields.io/badge/Updated-Every%204%20Hours-brightgreen)](https://jiangshou.duckdns.org)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
[![Website](https://img.shields.io/badge/🌐-jiangshou.duckdns.org-00d4aa)](https://jiangshou.duckdns.org)

## 📊 Live Data

| Asset | Price (USD) | 24h Change |
|-------|-------------|------------|
| **BTC** | Auto-updated | Auto-updated |
| **ETH** | Auto-updated | Auto-updated |
| **SOL** | Auto-updated | Auto-updated |

> 🔗 **[View live data →](https://jiangshou.duckdns.org)**

## 🚀 Quick Start

```bash
# Get latest prices
curl https://raw.githubusercontent.com/jiang-shou/crypto-data-feed/main/data/latest.json

# Get today's price history
curl https://raw.githubusercontent.com/jiang-shou/crypto-data-feed/main/data/prices_$(date +%Y-%m-%d).json
```

## 📁 Data Format

```json
{
  "updated": "2026-05-24T08:00:00Z",
  "btc": {"usd": 76781, "24h_change": 1.9, "market_cap": 1520000000000},
  "eth": {"usd": 2119, "24h_change": -0.5, "market_cap": 255000000000},
  "sol": {"usd": 86, "24h_change": 2.1, "market_cap": 38000000000}
}
```

## 🤖 Automation

- **Price data**: Updated every 4 hours via CoinGecko API
- **Historical**: Daily snapshots preserved
- **Reliability**: 99.97% uptime, running on dedicated infrastructure

## 📈 Pro Features

Need more than public data?

- 🔍 DEX arbitrage scanning
- 🐋 Whale address tracking  
- 📊 Market sentiment quantification
- 📱 Real-time Telegram alerts

→ **[Subscribe to JiangQuant Pro](https://jiangshou.duckdns.org/pricing)** · $10/month

## 📜 License

MIT — Free for any use. Data provided as-is, not financial advice.

---

<p align="center">
  <b>JiangQuant AI</b> · Autonomous Crypto Analytics Engine<br>
  <a href="https://jiangshou.duckdns.org">Website</a> · 
  <a href="https://t.me/jiangshou_bot">Telegram Bot</a> · 
  <a href="https://jiangshou.duckdns.org/pricing">Pro Subscription</a>
</p>
