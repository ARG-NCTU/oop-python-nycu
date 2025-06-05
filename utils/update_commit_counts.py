import json

# Step 1: Load the commit counts from txt file
commit_counts = {}
with open('utils/commit_counts.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if ':' in line:
            username, count = line.strip().split(':', 1)
            commit_counts[username.strip()] = int(count.strip())

# Step 2: Load the group data
try:
    with open('utils/group_status.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: group_status.json not found. Please ensure the file exists.")
    exit(1)

# Step 3: Update commit counts
for group in data:
    leader = group.get('group_leader', {})
    if leader.get('username') in commit_counts:
        leader['commits'] = commit_counts[leader['username']]
    for member in group.get('group_members', []):
        if member.get('username') in commit_counts:
            member['commits'] = commit_counts[member['username']]

# Step 4: Save the updated data back to JSON
with open('group_status.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Commit counts updated successfully.")
