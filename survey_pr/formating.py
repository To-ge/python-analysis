import pandas as pd
from github import Github

# GitHubのアクセストークンを設定
access_token = "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"
g = Github(access_token)

# リポジトリ情報
repo_owner = "spring-projects"
repo_name = "spring-framework"
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Pull Requestデータを取得
pulls = repo.get_pulls(state="all")[:100]

# 各プロパティごとのリストを初期化
numbers = []
titles = []
states = []
merged_statuses = []
created_dates = []
updated_dates = []
closed_dates = []
users = []
labels_lists = []

# プルリクエストデータを各プロパティごとにリストに追加
for pull in pulls:
    numbers.append(pull.number)
    titles.append(pull.title)
    states.append(pull.state)
    merged_statuses.append(pull.merged)
    created_dates.append(pull.created_at)
    updated_dates.append(pull.updated_at)
    closed_dates.append(pull.closed_at)
    users.append(pull.user.login)
    labels_lists.append([label.name for label in pull.labels])

# データをDataFrameに格納
data = {
    "Number": numbers,
    "Title": titles,
    "State": states,
    "Merged": merged_statuses,
    "Created Date": created_dates,
    "Updated Date": updated_dates,
    "Closed Date": closed_dates,
    "User": users,
    "Labels": labels_lists
}
df = pd.DataFrame(data)

# DataFrameをCSVファイルに保存
csv_file = "pull-requests.csv"
df.to_csv(csv_file, sep='\t', index=False)

print(f"Data saved to {csv_file}")
