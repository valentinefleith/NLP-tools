from Text import Text


import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage : py main.py /path/to/file.txt")
    text = Text(sys.argv[1])
    print(text.get_cleaned_lemmas())


if __name__ == "__main__":
    main()
