from os import listdir
from os.path import isfile, join
from .file import File

class Directory:

    def __init__(self, path):
        """ constructor """
        self._path = path
        self.files = []
        if isfile(self._path):
            self.files = [File(self._path)]
        else:
            self.collect_files()


    def collect_files(self):
        """ find all the files in dir """
        for f in listdir(self._path):
            if isfile(join(self._path, f)):
                self.files.append(File(self._path + f))

    def filter_files(self):
        """ filter all files in dir """
        for f in self.files:
            f.filter()

    def output(self):
        """ output all the files in dir to the user """
        self.header_output()
        for f in self.files:
            f.output()


    def header_output(self):
        """ outputs the dir header """
        print("# %s" %(self._path))
