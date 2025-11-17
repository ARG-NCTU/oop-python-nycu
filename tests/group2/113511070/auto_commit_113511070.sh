#!/bin/bash

# Step 1: 產生測試檔案
python3 generate_tests_113511070.py

# Step 2: 加入 git
git add .

# Step 3: 自動 commit（加上時間戳記）
git commit -m "Auto commit at $(date '+%Y-%m-%d %H:%M:%S') for 113511070"

# Step 4: 自動 push
git push origin main
