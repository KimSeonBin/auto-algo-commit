import os
import filepath
from datetime import datetime


class AlgoFiles:
    def __init__(self):
        self.files = []
        self.today = datetime.now()

    def __validate_file(self, filename, algopath):
        '''
        앞에 n이 붙어 있으면 아직 다 못 푼 문제.
        현재 날짜와 비교해서 같은 날짜이고 n이 붙어있지 않다면 푼 문제라고 판단
        '''
        if filename[0] is 'n':
            return False
        filename = algopath+"/"+filename
        filetime = datetime.fromtimestamp(os.path.getmtime(filename))

        if self.today.year != filetime.year or \
        self.today.month != filetime.month or \
        self.today.day != filetime.day:
            return False

        return True

    def get_algo_files(self):
        algo_path = filepath.get_algo_path()
        file_list = os.listdir(algo_path)

        for file in file_list:
            if self.__validate_file(file, algo_path):
                self.files.append(file)

        return self.files, algo_path
