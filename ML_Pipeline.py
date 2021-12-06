import git
import dvc.api
import pandas as pd
import mlflow

REPO_PATH = './'
REQUIRED_TAG = 'v1'
repo = git.Repo(REPO_PATH)


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
        return (str(commit.hexsha))
    else:
        return None


def get_commit_hexsha_by_tag(repo, required_tag):
    for tag in repo.tags:
        if tag.name == required_tag:
            return str(tag.commit.hexsha)


# print_repository_info(repo)
# x = print_commit_data(list(repo.iter_commits('main'))[0], 'v1')
# print(x)


# check that the repository loaded correctly
if not repo.bare:
    print('Repo is successfully loaded.')
    print_repository_info(repo)
    COMMITS_TO_PRINT = 10

    # create list of commits then print some of them to stdout
    commits = list(repo.iter_commits('main'))[:COMMITS_TO_PRINT]
    print("==================== Commits ====================")
    print("length of commits: ", len(commits), "===============")
    print(commits)

    commit_hexsha = get_commit_hexsha_by_tag(repo, REQUIRED_TAG)
    print('commit_hexsha: ', commit_hexsha)
    resource_url = dvc.api.get_url(
        path='data/Mall_Customers.csv',
        repo=REPO_PATH,
        rev=commit_hexsha,
        # rev=REQUIRED_TAG, # OR commit_hexsha
        # remote='dvc-RAM-remote'
    )
    print("==================== resource_url ====================")
    print(resource_url)

    df = pd.read_csv(resource_url, sep=',')
    print(len(df))
    display(df)

#     mlflow.set_tracking_uri('http://127.0.0.1:5000')
#     mlflow.set_experiment("/RAM-Pipeline")
#     with mlflow.start_run():
#         mlflow.log_param("Requested Version", req_ver)
#         mlflow.log_param("Requested Version path", resource_url)
#         mlflow.log_param("Requested Version Count", len(df))
# else:
#     print('Could not load repository at {} :'.format('repo_path'))
