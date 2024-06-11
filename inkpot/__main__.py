import sys
from inkpot.directory import Directory


def main():
    directory = Directory(sys.argv[1])
    directory.parse_files()
    directory.output()


if __name__ == "__main__":
    main()
