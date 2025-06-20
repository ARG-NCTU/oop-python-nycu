import pandas as pd
import argparse
import os

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

script_dir = os.path.dirname(os.path.abspath(__file__))

group_status_path = os.path.join(script_dir, 'group_status.json')
pytest_results_path = os.path.join(script_dir, 'pytest_results.txt')

df = pd.read_json(group_status_path)
curr_status = df['status'].tolist()

new_status = load_status(pytest_results_path)
if len(new_status) == len(curr_status):
    df['status'] = new_status
    df.to_json(group_status_path, orient='records', force_ascii=False)
else:
    print("Error: Status count mismatch. No update performed.")