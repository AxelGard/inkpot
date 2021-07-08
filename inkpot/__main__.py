import sys
from .directory import Directory


def main():
    dir = Directory(sys.argv[1])
    dir.parse_files()
    dir.output()


if __name__ == "__main__":
    main()
