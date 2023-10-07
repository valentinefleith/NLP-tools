import argparse

from tokenization import tokenize


def main():
    parser = argparse.ArgumentParser(
                    prog="py tokenization.py",
                    description='Tokenize a text file.')
    parser.add_argument('filename')
    args = parser.parse_args()
    file = args.filename
    tokens = create_dict(file)
    print(tokens)


def create_dict(file):
    words = tokenize(file)
    tokens = {}
    for element in words:
        if tokens.get(element):
            tokens[element] += 1
        else:
            tokens[element] = 1
    # tokens = sorted(tokens.items(), key=lambda x: x[1])
    return remove_empty_words(tokens)


def remove_empty_words(tokens):
    path = "/home/val/M1_TAL/Semestre_1/Programmation_algorithmique/exos_cours3/devoirs/tokenisation/aux/stop_words.txt"
    with open(path, "r") as empty_words:
        stop_words = empty_words.read()
        new_dict = {}
        for key in tokens:
            if (key) not in stop_words:
                new_dict[key] = tokens[key]
    return sort_dict(new_dict)


def sort_dict(tokens):
    sorted_dict = {}
    sorted_keys = sorted(tokens, key=tokens.get)
    for key in sorted_keys:
        sorted_dict[key] = tokens[key]
    return sorted_dict


if __name__ == "__main__":
    main()