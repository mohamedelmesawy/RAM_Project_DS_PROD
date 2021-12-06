import pprint
import git
import dvc.api
from git.exc import RepositoryDirtyError
import pandas as pd
import mlflow


repo = git.Repo('.git')


def print_repository_info(repo):
    print('Repository description: {}'.format(repo.description))
    print('Repository active branch is {}'.format(repo.active_branch))

    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))

    print('Last commit for repository is {}.'.format(
        str(repo.head.commit.hexsha)))


def print_commit_data(commit, req_ver):
    print('-----------------------------------')
    print('commit.hexsha:', str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary,
                                     commit.author.name, commit.author.email))
    print('commit.authored_datetime:', str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))
    if req_ver in commit.summary:
        return(str(commit.hexsha))
    else:
        return("")


# print_repository_info(repo)
# pprint.pprint(list(repo.iter_commits('main'))[0])
# print_commit_data(list(repo.iter_commits('main'))[0], 'v1')


# check that the repository loaded correctly
if not repo.bare:
    print('Repo at {} successfully loaded.')
    print_repository_info(repo)
    COMMITS_TO_PRINT = 10

    # create list of commits then print some of them to stdout
    commits = list(repo.iter_commits('main'))[:COMMITS_TO_PRINT]
    print("==================== Commits ====================")
    print(commits)
    print("length of commits", len(commits))

    number = 0
    rev1 = ""
    req_ver = "v2"

    while ((number < len(commits)) and rev1 == ""):
        print(f"Number is {number}!")
        rev1 = print_commit_data(commits[number], req_ver)
        number = number + 1

    print("rev1")
    print('CHECK MEEEEEEEEE', rev1)

    resource_url2 = dvc.api.get_url(
        'data/Mall_Customers.csv',
        repo=r".git",
        rev=rev1
    )
    print('-----')
    print(resource_url2)

    df = pd.read_csv(resource_url2, sep=',')
    print(len(df))
    display(df)

    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    mlflow.set_experiment("/RAM-Pipeline")
    with mlflow.start_run():
        mlflow.log_param("Requested Version", req_ver)
        mlflow.log_param("Requested Version path", resource_url2)
        mlflow.log_param("Requested Version Count", len(df))
else:
    print('Could not load repository at {} :'.format('repo_path'))
