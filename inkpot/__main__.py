import sys

from os import listdir
from os.path import isfile, join

from .filter import filter_file
from . import formator

def main():
    """ main function """
    given_path = sys.argv[1]
    formator.main_header(given_path)

    if not isfile(given_path): # is dir
        for f in listdir(given_path):
            if isfile(join(given_path, f)):
                handel_one_file(given_path + f)
    else:
        handel_one_file(given_path)

def handel_one_file(path_):
    """ generates a singel files output """
    file_info = filter_file(path_)
    formator.file_header(path_)
    formator.table_format(file_info)

if __name__ == "__main__":
    main()
