from datetime import datetime
from git import Repo
import shutil
import filepath


class GitFiles:
    def __init__(self, files, path):
        self.files = files
        self.ori_path = path
        self.backjoon_path = filepath.get_acmicpc_path()
        self.prog_path = filepath.get_programmers_path()

    def copy_files(self):
        for file in self.files:
            if file.find('pro') != -1:
                shutil.copy(src=self.ori_path+'/'+file, dst=self.prog_path)
            else:
                shutil.copy(src=self.ori_path+'/'+file, dst=self.backjoon_path)

    def __get_commit_message(self):
        today = datetime.now()
        return "{0:4d}.{1:02d}.{2:02d}".format(today.year, today.month, today.day)

    def git_commit_push(self):
        git_repo = Repo(filepath.get_git_repo_path())

        for file in self.files:
            if file.find('pro') != -1:
                git_repo.git.add(self.prog_path+'/'+file)
            else:
                git_repo.git.add(self.backjoon_path+'/'+file)
        git_repo.git.commit(m=self.__get_commit_message())
        git_repo.git.push("origin", "HEAD:master")
        '''
        https://stackoverflow.com/questions/50854924/push-to-remote-repository
        https://gitpython.readthedocs.io/en/stable/tutorial.html
        https://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work
        실행 스크립트 작성
        '''
