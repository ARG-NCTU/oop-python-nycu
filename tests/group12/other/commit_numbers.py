#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
count_commits_by_user.py
------------------------------------------------------------
用於查詢特定使用者在 ARG-NCTU/oop-python-nycu 專案中的 commit 次數。

支援三種查詢模式：
1️⃣ 查詢「某日期之前」的 commits
2️⃣ 查詢「某日期之後」的 commits
3️⃣ 查詢「某日期之間」的 commits

放置位置：
    tests/group12/other/count_commits_by_user.py
------------------------------------------------------------
"""

import requests
from datetime import datetime

# -------------------- GitHub 設定 --------------------
REPO_OWNER = "ARG-NCTU"
REPO_NAME = "oop-python-nycu"

# 可選：若頻繁查詢，建議填入個人 GitHub Token 以避免 API 限制
GITHUB_TOKEN = None  # 例如 "ghp_xxxYOURTOKENxxx"


# -------------------- 主查詢函式 --------------------
def count_commits(username, since=None, until=None, token=None):
    """
    計算特定使用者在指定時間內的 commit 次數
    從 ARG-NCTU/oop-python-nycu 取得資料
    """
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    params = {"author": username}
    if since:
        params["since"] = since + "T00:00:00Z"
    if until:
        params["until"] = until + "T23:59:59Z"

    total = 0
    page = 1

    while True:
        params["page"] = page
        params["per_page"] = 100
        r = requests.get(url, headers=headers, params=params)

        if r.status_code != 200:
            print(f"❌ API Error {r.status_code}: {r.text}")
            break

        commits = r.json()
        if not commits:
            break

        total += len(commits)
        page += 1

    return total


# -------------------- 主程式 --------------------
if __name__ == "__main__":
    print("🔍 GitHub Commit 查詢工具")
    print("📘 Repository: ARG-NCTU/oop-python-nycu\n")

    username = input("請輸入欲查詢的 GitHub 使用者名稱: ").strip()

    print("\n📅 選擇時間範圍模式：")
    print("1️⃣  某日期『之前』")
    print("2️⃣  某日期『之後』")
    print("3️⃣  某日期『之間』")
    mode = input("請輸入選項 (1/2/3): ").strip()

    since = until = None
    if mode == "1":
        until = input("請輸入截止日期 (YYYY-MM-DD): ").strip()
    elif mode == "2":
        since = input("請輸入起始日期 (YYYY-MM-DD): ").strip()
    elif mode == "3":
        since = input("請輸入起始日期 (YYYY-MM-DD): ").strip()
        until = input("請輸入結束日期 (YYYY-MM-DD): ").strip()
    else:
        print("⚠️ 無效的選項，程式結束。")
        exit(1)

    print("\n⏳ 正在查詢中，請稍候...\n")

    count = count_commits(
        username=username,
        since=since,
        until=until,
        token=GITHUB_TOKEN
    )

    if mode == "1":
        desc = f"{until} 之前"
    elif mode == "2":
        desc = f"{since} 之後"
    else:
        desc = f"{since} 至 {until} 之間"

    print(f"✅ 使用者「{username}」在「{REPO_OWNER}/{REPO_NAME}」於 {desc} 的 commit 次數為：{count}")
