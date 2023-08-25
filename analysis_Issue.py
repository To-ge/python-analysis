import matplotlib.pyplot as plt
from github import Github
from github import Auth
from datetime import datetime, timedelta

access_token = "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"
auth = Auth.Token(access_token)

g = Github(auth=auth)

owner = "spring-projects"
repo_name = "spring-framework"

repo = g.get_repo(f"{owner}/{repo_name}")
issues = repo.get_issues(state="all")[:38]

# Issue報告日を集計
issue_dates = []
for issue in issues:
,,issue_dates.append(issue.created_at.date())

# 週ごとにIssue報告数を集計
weekly_counts = {}
for date in issue_dates:
    week_start = date
    if week_start in weekly_counts:
        weekly_counts[week_start] += 1
    else:
        weekly_counts[week_start] = 1

# 集計結果を表示
for week, count in weekly_counts.items():
    print(f"Week: {week}, Issue Count: {count}")

# 集計結果を可視化
weeks = list(weekly_counts.keys())
counts = list(weekly_counts.values())

plt.figure(figsize=(10, 6))
plt.bar(weeks, counts, align="center", color="blue")
plt.xlabel("Week")
plt.ylabel("Issue Count")
plt.title(f"Issue Report Count for {owner}/{repo_name} by Week")
plt.xticks(weeks, [week.strftime("%Y-%m-%d") for week in weeks], rotation=45)
plt.tight_layout()
plt.show()
