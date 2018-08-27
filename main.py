from algofiles import AlgoFiles
from gitfiles import GitFiles

def start():
    algo_files = AlgoFiles()
    today_files, filepath = algo_files.get_algo_files()

    git_files = GitFiles(today_files, filepath)
    print(git_files.files)

    git_files.copy_files()
    git_files.git_commit_push()



if __name__ == "__main__":
    start()
