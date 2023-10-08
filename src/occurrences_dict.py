import sys

from tokenization import tokenize


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage : py create_dict_tokens.py /path/to/file.txt")
    file = sys.argv[1]
    tokens = create_dict(file)
    tokens = remove_empty_words(tokens)
    tokens = sort_dict(tokens)
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
    return tokens


def remove_empty_words(tokens):
    path = "/home/val/M1_TAL/Semestre_1/Programmation_algorithmique/exos_cours3/devoirs/tokenisation/aux/stop_words.txt"
    with open(path, "r") as empty_words:
        stop_words = empty_words.read()
        new_dict = {key: tokens[key] for key in tokens if key not in stop_words}
    return new_dict


def sort_dict(tokens):
    sorted_keys = sorted(tokens, key=tokens.get)
    sorted_dict = {key: tokens[key] for key in sorted_keys}
    return sorted_dict


if __name__ == "__main__":
    main()
