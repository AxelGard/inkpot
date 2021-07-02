import sys
from .filter import filter_file
from .formator import table_format

def main():
    """ main function """
    file_info = filter_file(sys.argv[1])
    table_format(file_info)


if __name__ == "__main__":
    main()
