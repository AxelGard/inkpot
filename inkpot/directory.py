"""
class instance for a directory
"""

from os import walk
from os.path import isfile
from .file import File


class Directory:
    """ Directory is for interacting with a directory and its subdirs """

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
        for path, subdirs, files in walk(self._path):
            for f in files:
                if f.endswith(".py"):
                    self.files.append(File(f"{path}/{f}"))

    def parse_files(self):
        """ filter all files in dir """
        for f in self.files:
            f.parse()

    def output(self):
        """ output all the files in dir to the user """
        self.header_output()
        for f in self.files:
            f.output()

    def header_output(self):
        """ outputs the dir header """
        print("# %s" % (self._path))
