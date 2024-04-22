import subprocess
import argparse
from collections import defaultdict
from datetime import datetime, timedelta

def set_safe_directory(repo_path):
    # Command to set the safe directory for Git
    cmd = ["git", "config", "--global", "--add", "safe.directory", repo_path]
    try:
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # print("Repository set as safe successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to set safe directory:", e)
        return False
    return True

def get_commits_by_user(repo_path, username=None):
    # Ensure the repository is considered 'safe' by Git
    if not set_safe_directory(repo_path):
        return
    
    # Navigate to the repository
    try:
        subprocess.check_call(["git", "-C", repo_path, "status"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("Failed to access repository. Check the repository path.")
        return
    
    # Define the time period: from 3 months ago to now
    since_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

    # Prepare git log command
    cmd = ["git", "-C", repo_path, "log", "--since", since_date, "--pretty=format:%H;%an"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.stderr:
        print("Error retrieving commits:", result.stderr)
        return
    
    # Organize commits by user
    commits_by_user = defaultdict(int)
    for line in result.stdout.strip().split('\n'):
        commit_hash, author = line.split(';')
        commits_by_user[author] += 1

    # Return total commits for the specified user or all users if no username is specified
    if username:
        commit_count = commits_by_user.get(username, 0)
        if commit_count > 0:
            print(f"User: {username}, Commit Count: {commit_count}")
        else:
            print(f"No commits found for user '{username}'. This might be due to a wrong username or the user made no commits in the last 3 months.")
    else:
        for user, count in commits_by_user.items():
            print(f"User: {user}, Commit Count: {count}")
        print("\nNo username specified. Displaying all users' commit counts above.")
        print("To filter by a specific user, use the '--user' argument followed by the username.")
        print("Example: python3 git_commit_num.py --user username")


def main():
    parser = argparse.ArgumentParser(description='Get commit counts by user from a git repository.')
    parser.add_argument('--user', type=str, help='Username to filter commit counts by.')
    parser.add_argument('--repo', type=str, default='/home/arg/oop-python-nycu', help='Path to the git repository.')
    args = parser.parse_args()

    get_commits_by_user(args.repo, args.user)

if __name__ == '__main__':
    main()
