from git import Repo

clone_dir = "../datas/apache"
repo_url = "https://github.com/apache/commons-math"

repo = Repo.clone_from(repo_url, clone_dir)

print(f"Repository cloned to {clone_dir}")
