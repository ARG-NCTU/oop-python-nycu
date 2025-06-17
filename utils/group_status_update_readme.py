import pandas as pd
import json

# --- 1. 載入 JSON 檔案 ---
# 這會將 JSON 檔案的內容讀取成一個 Python 列表 (list)，其中每個元素是一個字典 (dict)
try:
    with open('group_status.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: groups_data.json not found. Please ensure the file exists.")
    exit(1) # 如果檔案不存在，程式直接退出

# --- 2. 扁平化數據：使用 pd.json_normalize ---
# pd.json_normalize 適合處理列表中的字典，並能展開嵌套結構。
# 我們先處理頂層數據和 'group_leader' 的信息。
# 'meta' 參數用於指定要從原始數據中保留下來的頂層欄位。
# 我們需要 'status', 'group_name', 'group_leader' 和 'group_members'。
# 注意：這裡我們暫時不展開 'group_members'，因為它們是列表，需要額外處理。
df_normalized = pd.json_normalize(data,
                                  # record_path=None 表示不展開任何列表，只處理頂層和嵌套字典
                                  # meta 指定要從原始數據中提取的頂層鍵
                                  # [key, nested_key] 用於提取嵌套字典中的值
                                  meta=['status', 'group_name',
                                        ['group_leader', 'username'],
                                        ['group_leader', 'commits']],
                                  # 如果有 'group_members' 這種列表，它會保持為列表形式
                                  errors='ignore')

# 重命名一些扁平化後的列，讓它們更清晰
df_normalized = df_normalized.rename(columns={
    'group_leader.username': 'leader_username',
    'group_leader.commits': 'leader_commits'
})

# --- 3. 處理 'group_members' 列表欄位 ---
# 'group_members' 是一個列表，每個元素又是一個字典 (username, commits)。
# 我們需要將它轉換成符合你表格需求的字串格式，例如 "username : commits"。
# 並且需要處理表格中 Group Member 1 和 Group Member 2 兩列。

def format_members_for_table(members_list):
    """將成員列表格式化為 'username : commits' 字串列表"""
    formatted = []
    if members_list:
        for member in members_list:
            if isinstance(member, dict) and 'username' in member and 'commits' in member:
                formatted.append(f"{member['username']} : {member['commits']}")
    return formatted

# 將 'group_members' 欄位應用格式化函數
df_normalized['formatted_members'] = df_normalized['group_members'].apply(format_members_for_table)

# --- 4. 建立最終表格所需的欄位 ---
# 根據你的 README 表格，需要 Group Leader, Group Member 1, Group Member 2

# 組合 Group Leader 欄位
df_normalized['Group Leader'] = df_normalized.apply(
    lambda row: f"{row['leader_username']} : {row['leader_commits']}" if pd.notna(row['leader_username']) else '',
    axis=1
)

# 分配 Group Member 1 和 Group Member 2
# 注意：這裡假設最多只有兩個組員，如果有可能更多，你需要擴展這個邏輯
df_normalized['Group Member 1'] = df_normalized['formatted_members'].apply(
    lambda x: x[0] if len(x) > 0 else ''
)
df_normalized['Group Member 2'] = df_normalized['formatted_members'].apply(
    lambda x: x[1] if len(x) > 1 else ''
)

# --- 5. 選擇最終需要的欄位並重新排序 ---
# 這些欄位將直接對應到你的 Markdown 表格列
final_df = df_normalized[[
    'status',
    'group_name',
    'Group Leader',
    'Group Member 1',
    'Group Member 2'
]]

# --- 6. 轉換為 Markdown 表格字串 ---
# to_markdown() 是一個非常方便的函數，能直接生成 Markdown 表格
# index=False 表示不包含 DataFrame 的索引列
markdown_table_string = final_df.to_markdown(index=False)

# --- 7. 輸出 Markdown 表格字串 ---
print(markdown_table_string)

# 你現在可以用這個 markdown_table_string 去更新 README.md 了
# 後續步驟：讀取 README.md，找到標記，替換內容，然後寫回。

# --- 8. 更新 README.md 中的指定區塊 (不使用 re) ---

readme_path = 'README.md'
start_marker = '<!--START_SECTION:pytest-->'
end_marker = '<!--END_SECTION:pytest-->'

try:
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: {readme_path} not found.")
    exit(1)

start_idx = end_idx = None
for i, line in enumerate(lines):
    if start_marker in line:
        start_idx = i
    if end_marker in line:
        end_idx = i
        break

if start_idx is None or end_idx is None or start_idx >= end_idx:
    print("Markers not found in README.md. No changes made.")
    exit(1)

# 保留 start_marker 行和 end_marker 行，中間替換為 markdown_table_string
new_lines = (
    lines[:start_idx + 1] +
    ['\n', markdown_table_string + '\n'] +
    lines[end_idx:]
)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("README.md updated successfully.")