from git import Repo

cloned_dir = "../datas/apache"

repo = Repo(cloned_dir)

latest_commit = repo.head.commit

# 最新のコミットにチェックアウト
repo.git.checkout(latest_commit)

# チェックアウトが完了したらメッセージを表示
print(f"Checked out to the latest commit: {latest_commit}")

commit_hash = "68f3d64fee929929b7f1c21a658aeb186a9cf697"

# コミットオブジェクトを取得
commit = repo.commit(latest_commit)

# コミットの内容（diff）を表示
print(commit.diff())

# コミットのメッセージを表示
print(f"commit.message{commit.message}")
print('-' * 50, '\n')

commits = list(repo.iter_commits())

# 各コミット情報を表示
for commit in commits:
    print("Commit Hash:", commit.hexsha)
    print("Message:", commit.message)
    print("Author:", commit.author.name)
    print("Date:", commit.authored_datetime)

    # コミットの変更情報（diff）を取得
    diff = commit.diff()

    # 変更ファイルと変更行数を表示
    for change in diff:
        if change.change_type == 'M' or change.change_type == 'A' or change.change_type == 'D':
            if change.diff:
                print("Changed File:", change.a_path)
                print("Change Type:", change.change_type)
                lines_added = change.diff.splitlines()
                lines_removed = change.diff.splitlines()
                print("Lines Added:", len(lines_added))
                print("Lines Removed:", len(lines_removed))
    print("=" * 50)
