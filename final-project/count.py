import requests

def get_commit_count(repo_owner, repo_name, username, token):
    """
    計算特定使用者在某個GitHub儲存庫中的commit次數。

    :param repo_owner: 儲存庫擁有者的GitHub帳號名稱。
    :param repo_name: 儲存庫名稱。
    :param username: 要查詢的使用者名稱。
    :param token: 個人存取權杖（Personal Access Token），用於驗證API請求。
    :return: commit次數。
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    headers = {
        'Authorization': f'token {token}'
    }
    params = {
        'author': username
    }

    commit_count = 0
    while url:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return None

        commits = response.json()
        commit_count += len(commits)

        # 分頁處理，檢查Link標頭是否包含下一頁
        if 'Link' in response.headers:
            links = response.headers['Link']
            next_link = None
            for link in links.split(','):
                if 'rel="next"' in link:
                    next_link = link.split(';')[0].strip().strip('<>').strip()
                    break
            url = next_link
        else:
            url = None

    return commit_count

# 使用範例
if __name__ == "__main__":
    repo_owner = "octocat"  # 替換為儲存庫擁有者名稱
    repo_name = "Hello-World"  # 替換為儲存庫名稱
    username = "octocat"  # 替換為要查詢的使用者名稱
    token = "your_personal_access_token"  # 替換為您的GitHub個人存取權杖

    commit_count = get_commit_count(repo_owner, repo_name, username, token)

    if commit_count is not None:
        print(f"使用者 {username} 在儲存庫 {repo_owner}/{repo_name} 中的 commit 次數為: {commit_count}")

