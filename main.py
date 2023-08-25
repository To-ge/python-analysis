from github import Github
from github import Auth
import requests

access_token = "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"
auth = Auth.Token(access_token)

g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(auth=auth)

# Then play with your Github objects:
print('b')
for repo in g.get_user().get_repos():
    commits = repo.get_commits().totalCount
    print(f"{repo.name}: {commits}")

print('\nc')
popular_repositories = g.search_repositories(query="all", sort="stars", order="desc")[:10]

for i, repo in enumerate(popular_repositories):
    print(f"{i+1} {repo.name} スター数: {repo.stargazers_count}")

print('\nJava:')
java_repositories = g.search_repositories("language:java", sort="stars", order="desc")[:10]
for i, repo in enumerate(java_repositories):
    print(f"{i+1} {repo.name} スター数: {repo.stargazers_count}")

print('\nPython:')
python_repositories = g.search_repositories("language:python", sort="stars", order="desc")[:10]
for i, repo in enumerate(python_repositories):
    print(f"{i+1} {repo.name} スター数: {repo.stargazers_count}")

print('\nd')
repo_owner = "spring-projects"
repo_name = "spring-framework"
repo = g.get_repo(f"{repo_owner}/{repo_name}")

for issue in repo.get_issues(state="all")[:3]:
    print(f"Issue #{issue.number}: {issue.title}")
    print(f"State: {issue.state}")
    print(f"Created by: {issue.user.login}")
    print(f"Created at: {issue.created_at}")
    print(f"Updated at: {issue.updated_at}")
    print(f"Comments: {issue.comments}")
    print("-----")

print('\ne')
pull_requests = repo.get_pulls(state="all")

for pr in pull_requests[:5]:
    print(f"PR #{pr.number}: {pr.title}")
    print(f"State: {pr.state}")
    print(f"Created At: {pr.created_at}")
    print(f"Closed At: {pr.closed_at}")
    print(f"URL: {pr.html_url}")
    print("-" * 30)

rejected_pull_requests = repo.get_pulls(state="closed", sort="created", direction="desc")
rejected_pr_count = 0

for pr in pull_requests[:100]:
    if pr.state == "closed" and pr.merged_at is None and pr.closed_at is not None:
        rejected_pr_count += 1

print(f"Rejected Pull Requests: {rejected_pr_count}")

api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/runs"
response = requests.get(api_url)
data = response.json()

# ビルド結果を処理して失敗したビルドの数をカウント
failed_builds = 0
total_builds = 0

for run in data['workflow_runs']:
    total_builds += 1
    if run['conclusion'] == "failure":
        failed_builds += 1

# 失敗したビルドの割合を計算
failure_rate = (failed_builds / total_builds) * 100

print(f"Total builds: {total_builds}")
print(f"Failed builds: {failed_builds}")
print(f"Failure rate: {failure_rate:.2f}%")
