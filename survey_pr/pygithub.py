from github import Github
from github import Auth

access_token = "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"
auth = Auth.Token(access_token)

g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(auth=auth)

repo_owner = "spring-projects"
repo_name = "spring-framework"
repo = g.get_repo(f"{repo_owner}/{repo_name}")

pull_requests = repo.get_pulls(state='closed', sort='created', direction='desc',
                               base='master')

# プルリクエストごとに関連するコミットを表示
for pr in pull_requests:
    print(f"PR Number: {pr.number}")
    print(f"Title: {pr.title}")

    # プルリクエストに関連するコミットを取得
    commits = pr.get_commits()[:30]
    for commit in commits:
        print(f"Commit SHA: {commit.sha}")
        print(f"Author: {commit.author.login}")
        print(f"Date: {commit.commit.author.date}")
        print(f"Message: {commit.commit.message}\n")
