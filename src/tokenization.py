"""
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage : py tokenization.py /path/to/file.txt")
    print(tokenize(sys.argv[1]))
"""

from lemmatization import lemmatize


def tokenize(file):
    with open(file, "r") as text:
        lemmas = lemmatize(text.read())
        words = clean_text(lemmas).split()
    words += split_apostrophes(words)
    return words


def clean_text(text):
    cleaned = ""
    for char in text:
        if char == "\n":
            cleaned += " "
        if char not in "?!():;.,«»–¬—*":
            cleaned += char.lower()
    return cleaned


def split_apostrophes(text):
    # apostrophe = "'"
    apostrophe = "’"
    apostrophes = []
    indexes = []
    for index, word in enumerate(text):
        if apostrophe in word:
            temp = word.split(apostrophe)
            apostrophes.append(temp[0] + apostrophe)
            apostrophes.append(temp[1])
            indexes.append(index)
    indexes.reverse()
    for i in indexes:
        text.pop(i)
    return apostrophes


"""
if __name__ == "__main__":
    main()
"""
