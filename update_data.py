#!/usr/bin/env python3
"""Auto-update crypto price data for GitHub open dataset"""
import json, os, time, urllib.request

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fetch from CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"
req = urllib.request.Request(url, headers={"User-Agent": "JiangQuant/1.0"})
with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode())

prices = {
    "updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "btc": {"usd": data["bitcoin"]["usd"], "24h_change": data["bitcoin"].get("usd_24h_change", 0), "market_cap": data["bitcoin"].get("usd_market_cap", 0)},
    "eth": {"usd": data["ethereum"]["usd"], "24h_change": data["ethereum"].get("usd_24h_change", 0), "market_cap": data["ethereum"].get("usd_market_cap", 0)},
    "sol": {"usd": data["solana"]["usd"], "24h_change": data["solana"].get("usd_24h_change", 0), "market_cap": data["solana"].get("usd_market_cap", 0)}
}

# Save latest
with open(os.path.join(OUTPUT_DIR, "latest.json"), "w") as f:
    json.dump(prices, f, indent=2)

# Save historical (append to daily file)
daily_file = os.path.join(OUTPUT_DIR, f"prices_{time.strftime('%Y-%m-%d')}.json")
daily_data = []
if os.path.exists(daily_file):
    with open(daily_file) as f:
        daily_data = json.load(f)
daily_data.append(prices)
with open(daily_file, "w") as f:
    json.dump(daily_data, f, indent=2)

print(f"Updated: BTC ${data['bitcoin']['usd']:,} | ETH ${data['ethereum']['usd']:,} | SOL ${data['solana']['usd']}")
