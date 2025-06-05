import pandas as pd
import argparse

def load_status(file_path):
    statuses = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line or ": " not in line:
                continue
            grp, st = line.strip().split(": ", 1)
            if st == "success":
                st = "✅"
            elif st == "failed":
                st = "❌"
            statuses.append(st)
    return statuses

df = pd.read_json('utils/group_status.json')
curr_status = df['status'].tolist()

new_status = load_status('utils/pytest_results.txt')
if len(new_status) == len(curr_status):
    df['status'] = new_status
    df.to_json('group_status.json', orient='records', force_ascii=False)
else:
    print("Error: Status count mismatch. No update performed.")