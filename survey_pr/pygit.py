import pygit2

# spring-framework リポジトリのクローンを作成
cloned_dir = "../datas/spring-framework"

# repo_url = "https://github.com/spring-projects/spring-framework"
# repo_path = "../datas/spring-framework"

repo = pygit2.Repository(cloned_dir)
# repo = pygit2.clone_repository(repo_url, repo_path)

for commit in repo.walk(repo.head.target, pygit2.GIT_SORT_TIME):
    # コミットメッセージを取得
    commit_message = commit.message

    # 変更されたファイル数と行数を初期化
    num_changed_files = 0
    num_added_lines = 0
    num_removed_lines = 0

    # コミットの親コミットを取得
    parents = commit.parents

    # 最初のコミットの場合は差分を計算できないためスキップ
    if len(parents) == 0:
        continue

    # 差分を計算
    diff = repo.diff(parents[0], commit)

    # 変更されたファイルと行数を集計
    for patch in diff:
        num_changed_files += 1
        num_added_lines += patch.line_stats[1]
        num_removed_lines += patch.line_stats[2]

    # 収集したメトリクスを表示
    print("Commit:", commit.id)
    print("Commit Message:", commit_message)
    print("Number of Changed Files:", num_changed_files)
    print("Number of Added Lines:", num_added_lines)
    print("Number of Removed Lines:", num_removed_lines)
    print("-----------------------------------")
