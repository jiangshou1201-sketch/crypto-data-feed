#!/bin/bash
cd /home/ubuntu/crypto-data-feed
python3 update_data.py
git add data/
git commit -m "Auto-update: $(date -u +'%Y-%m-%d %H:%M UTC')" 2>/dev/null
git push origin master 2>&1
