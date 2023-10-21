from Text import Text
from Tokens import Tokens


import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage : py main.py /path/to/file.txt")
    text = Text(sys.argv[1])
    tokens = Tokens(text)
    print(tokens.occ_dict)


if __name__ == "__main__":
    main()
