#!/bin/bash
cd /home/ubuntu/crypto-data-feed
# Retry loop for CoinGecko rate limits (free tier: ~10-30 req/min)
for attempt in 1 2 3; do
    python3 update_data.py && break
    echo "Attempt $attempt failed, waiting 30s..." >&2
    sleep 30
done || exit 1

git add data/
git commit -m "Auto-update: $(date -u +'%Y-%m-%d %H:%M UTC')" 2>/dev/null
git push origin master 2>&1
