#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
count_commits_by_user.py
用來查詢特定 GitHub 帳號在特定時間區間內的 commit 次數。
可查詢：
 - 某日期之前的 commit
 - 某日期之後的 commit
 - 某日期至某日期之間的 commit

放置位置建議：
    tests/group12/other/count_commits_by_user.py
"""

import requests
from datetime import datetime

# -------------------- 可選：填入 GitHub Token --------------------
# 沒有 token 時，每小時 API 請求上限只有 60 次
GITHUB_TOKEN = None  # e.g. "ghp_xxxYOURTOKENHERExxx"

# -------------------- 查詢函式 --------------------
def count_commits(user, repo_owner, repo_name, since=None, until=None, token=None):
    """
    計算特定使用者在指定時間內的 commit 次數。
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    params = {"author": user}
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


# -------------------- 主程式邏輯 --------------------
if __name__ == "__main__":
    print("🔍 GitHub Commit 查詢工具")
    repo_owner = input("請輸入 Repository 擁有者 (例如 jui-pixel): ").strip()
    repo_name = input("請輸入 Repository 名稱 (例如 oop-python-nycu): ").strip()
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
        user=username,
        repo_owner=repo_owner,
        repo_name=repo_name,
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

    print(f"✅ 使用者「{username}」在「{repo_name}」於 {desc} 的 commit 次數為：{count}")
