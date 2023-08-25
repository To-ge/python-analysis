from github import Github
import matplotlib.pyplot as plt
import scipy.stats as stats

# GitHubのアクセストークンをセット
access_token = "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"
g = Github(access_token)

# リポジトリのオーナーと名前
repo_owner = "spring-projects"
repo_name = "spring-framework"

# リポジトリを取得
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# 受理されたPRと却下されたPRのデータを格納するリスト
accepted_prs = []
rejected_prs = []

# PRデータを取得して分類
for pr in repo.get_pulls(state="all")[:50]:
    if pr.state == "closed":
        if pr.merged:
            accepted_prs.append(pr)
        else:
            rejected_prs.append(pr)

# 受理されたPRと却下されたPRの数値データを取得
accepted_pr_numbers = [pr.number for pr in accepted_prs]
rejected_pr_numbers = [pr.number for pr in rejected_prs]

# 箱ひげ図を作成して可視化
plt.boxplot([accepted_pr_numbers, rejected_pr_numbers], labels=["Accepted PR", "Rejected PR"])
plt.title("Accepted vs Rejected Pull Requests")
plt.ylabel("PR Number")
plt.show()

statistic, p_value = stats.mannwhitneyu(accepted_pr_numbers, rejected_pr_numbers, alternative='two-sided')

# p値を表示
print("p-value:", p_value)

# p値をもとに有意差の判定
alpha = 0.05  # 有意水準（例：0.05）
if p_value < alpha:
    print("有意差がある")
else:
    print("有意差はない")
