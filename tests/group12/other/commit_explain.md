
---

# commit_calculator 原理分析

## 一、程式目的

`commit_numbers.py` 是用來 **計算特定 GitHub 使用者在特定專案中的提交次數 (commit)** 的工具。

它的功能包括：

1. 指定帳號 → 查詢該使用者的 commit。
2. 指定時間範圍 → 可查：

   * 某日期之前的 commit
   * 某日期之後的 commit
   * 某日期至某日期之間的 commit
3. 顯示統計結果 → 顯示 commit 的總次數。

> 簡單來說，就是統計「誰在什麼時間對專案做了多少貢獻」。

---

## 二、GitHub Commit 原理

### 1. GitHub Repo 與 commit

* **Repo（Repository）**：Git 專案倉庫，用來儲存程式碼。
* **Commit**：每一次對專案的修改紀錄，都會被記錄成 commit。
* **Author / Committer**：

  * `author`：原始提交者。
  * `committer`：實際執行 commit 的人（一般跟 author 相同）。

在程式中，我們以 `author` 來計算某使用者的貢獻。

### 2. GitHub API

GitHub 提供 **REST API** 來查詢專案資訊，例如：

```
https://api.github.com/repos/ARG-NCTU/oop-python-nycu/commits
```

透過參數，我們可以：

* `author=username` → 限制只查某使用者的 commit
* `since=YYYY-MM-DDT00:00:00Z` → 查詢指定日期之後
* `until=YYYY-MM-DDT23:59:59Z` → 查詢指定日期之前
* `page` 與 `per_page` → 分頁控制，避免一次傳回過多資料

---

## 三、程式原理

程式主要分為三個部分：

### 1. 固定 Repo 與輸入使用者

```python
REPO_OWNER = "ARG-NCTU"
REPO_NAME = "oop-python-nycu"
username = input("請輸入欲查詢的 GitHub 使用者名稱: ").strip()
```

* 專案固定，不讓使用者改動。
* 讓使用者只需輸入 GitHub 帳號即可。

### 2. 選擇時間範圍

使用者可選：

* **模式 1**：「某日期之前」
* **模式 2**：「某日期之後」
* **模式 3**：「某日期至某日期」

程式會根據選項，設定 `since` 和 `until` 參數：

```python
if mode == "1":
    until = input("請輸入截止日期 (YYYY-MM-DD): ").strip()
elif mode == "2":
    since = input("請輸入起始日期 (YYYY-MM-DD): ").strip()
elif mode == "3":
    since = input("請輸入起始日期 (YYYY-MM-DD): ").strip()
    until = input("請輸入結束日期 (YYYY-MM-DD): ").strip()
```

> 例如：
>
> * 選「之前」並輸入 `2025-10-01` → 查 2025-10-01 以前的 commit
> * 選「之間」並輸入 `2025-01-01` 到 `2025-10-01` → 查此區間的 commit

### 3. 查詢 GitHub API

程式使用 `requests` 模組呼叫 GitHub API：

```python
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
params = {"author": username}
if since: params["since"] = since + "T00:00:00Z"
if until: params["until"] = until + "T23:59:59Z"
```

#### 分頁處理

GitHub API 每次最多回傳 100 筆 commit，因此程式使用迴圈分頁查詢：

```python
total = 0
page = 1
while True:
    params["page"] = page
    params["per_page"] = 100
    r = requests.get(url, headers=headers, params=params)
    commits = r.json()
    if not commits:
        break
    total += len(commits)
    page += 1
```

> **原理說明**：
>
> * `page=1` → 第一頁 commit
> * `per_page=100` → 每頁最多 100 筆
> * 若回傳空列表 → 代表已查詢到最後一頁 → 結束迴圈
> * 每頁的 commit 數累加到 `total`

### 4. 顯示結果

```python
print(f"使用者「{username}」在「{REPO_OWNER}/{REPO_NAME}」於 {desc} 的 commit 次數為：{count}")
```

* `desc` 會根據時間範圍顯示「之前 / 之後 / 之間」
* `count` 是累計的 commit 次數

---

## 四、程式流程圖（簡單示意）

```
使用者輸入 GitHub 帳號
         │
         ▼
選擇時間範圍（之前 / 之後 / 之間）
         │
         ▼
設定 since / until 參數
         │
         ▼
呼叫 GitHub API (分頁查詢)
         │
         ▼
計算 commit 總數
         │
         ▼
顯示結果給使用者
```

---

## 五、程式特點與補充

1. **簡單易用**：只需帳號和時間範圍，不需要登入 GitHub（但未登入會受 API 限制，每小時最多 60 次）。
2. **分頁處理**：可應付大量 commit，保證計數正確。
3. **時間範圍靈活**：可自由查詢之前、之後或區間。
4. **可擴展性**：

   * 可加入 `branch` 選項 → 查所有 branch commit
   * 可將結果寫入 CSV → 建立統計紀錄

---

## 六、舉例說明

假設使用者輸入：

* 帳號：`jui-pixel`
* 時間範圍：2025-01-01 至 2025-10-01

程式會：

1. 設定 `author=jui-pixel`
2. 設定 `since=2025-01-01T00:00:00Z`，`until=2025-10-01T23:59:59Z`
3. 呼叫 API，查詢所有 commit
4. 計算總數，例如：42 次
5. 輸出：

```
使用者「jui-pixel」在「ARG-NCTU/oop-python-nycu」於 2025-01-01 至 2025-10-01 之間的 commit 次數為：42
```

