from git_commit_count import get_commits_by_user
import argparse
import xlsxwriter

def main():

    parser = argparse.ArgumentParser(description='Get commit counts by user from a git repository.')
    parser.add_argument('--repo', type=str, default='/home/arg/oop-python-nycu', help='Path to the git repository.')
    parser.add_argument('--start_date', type=str, default='2024-09-29', help='Start date for commit count calculation. Format: YYYY-MM-DD', nargs='?')
    args = parser.parse_args()

    github_accounts = [
        ["LeeYinWei", "unknown899"],    # Group 1
        [],  # Group 2
        [],  # Group 3
        [],  # Group 4
        [],  # Group 5
        ["jui-pixel", "SamTung113511034", "charles691"],  # Group 6
        ["Tony104147"], # Group 7
        ["haleychang0530", "Hazel-1212", "tree1014"],   # Group 8
        [],  # Group 9
        ["tpvupu", "xiaotin22", "calistayang"],  # Group 10
        [],  # Group 11
        [],  # Group 12
        [],  # Group 13
        ["weiouo-0817"],  # Group 14
        [],  # Group 15
        [],  # Group 16
        [],  # Group 17
        [],  # Group 18
        ["113511080", "max052028"],  # Group 19
        ["houyuankai"],  # Group 20
        ["0u88"]  # Group 21
    ]

    commits_by_users = [[] for _ in range(len(github_accounts))]

    # Iterate over the list of GitHub accounts
    for i, accounts in enumerate(github_accounts):
        for account in accounts:
            commit_count = get_commits_by_user(args.repo, account, args.start_date)
            if commit_count is None:
                commits_by_users[i].append(0)
            else:
                commits_by_users[i].append(commit_count)

    # Print the commit counts for each user
    for i, accounts in enumerate(github_accounts):
        print(f"Group {i+1}:")
        for j, account in enumerate(accounts):
            if account == "":
                continue
            print(f"User: {account}, Commit Count: {commits_by_users[i][j]}")

    # Export the commit counts to a xlsx file
    workbook = xlsxwriter.Workbook('commit_counts.xlsx')
    worksheet = workbook.add_worksheet('github_commit')
    worksheet.write(0, 0, "Group")
    worksheet.write(0, 1, "Group Leader")
    worksheet.write(0, 2, "Group Member")
    worksheet.write(0, 3, "Group Member")
    worksheet.write(0, 4, "Group Member")
    for i, accounts in enumerate(github_accounts):
        worksheet.write(i+1, 0, f"Group {i+1}")
        for j, account in enumerate(accounts):
            if account == "":
                continue
            worksheet.write(i+1, j+1, f"{github_accounts[i][j]} : {commits_by_users[i][j]}")
    workbook.close()

if __name__ == '__main__':
    main()

