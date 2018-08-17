from datetime import datetime
from git import Repo
import shutil
import filepath


class GitFiles:
    def __init__(self, files, path):
        self.files = files
        self.ori_path = path
        self.target_path = filepath.get_acmicpc_path()

    def copy_files(self):
        for file in self.files:
            shutil.copy(src=self.ori_path+'/'+file, dst=self.target_path)

    def __get_commit_message(self):
        today = datetime.now()
        return "{0:4d}.{1:02d}.{2:02d}".format(today.year, today.month, today.day)

    def git_commit_push(self):
        git_repo = Repo(filepath.get_git_repo_path())

        for file in self.files:
            git_repo.git.add(self.target_path+'/'+file)
        git_repo.git.commit(m=self.__get_commit_message())
        #git_repo.git.push("origin", "master")
        '''
        https://stackoverflow.com/questions/50854924/push-to-remote-repository
        https://gitpython.readthedocs.io/en/stable/tutorial.html
        https://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work
        
        '''