import sys

import occurrences_dict


def main():
    """
    This module prints relative frequencies of each word in text.
    -----------
    Argument 1 : path to text file
    Argument 2 (optional) : number of words to print.
        example 10 will print the 10 most common words and their frequency
    """
    if not 2 <= len(sys.argv) <= 3:
        sys.exit("Usage : py stats.py /path/to/file.txt (optional integer)")

    tokens = occurrences_dict.create_dict(sys.argv[1])
    tokens = occurrences_dict.sort_dict(occurrences_dict.remove_empty_words(tokens))
    frequencies = find_relative_frequency(tokens)
    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        print_x_first_frequencies(frequencies, int(sys.argv[2]))
    else:
        print(frequencies)


def find_relative_frequency(tokens):
    NUMBER_OF_TOKENS = len(tokens)
    frequencies = {}
    for key in tokens:
        frequency = round(tokens[key] * 100 / NUMBER_OF_TOKENS, 2)
        frequencies[key] = frequency
        # print(f"Frequence du mot {key} : {frequency}%")
    return frequencies


def print_x_first_frequencies(frequencies, number):
    counter = 1
    while counter <= number:
        i = -counter
        key = list(frequencies)[i]
        print(f"{counter}) Frequence du mot {key} : {frequencies[key]}%")
        counter += 1


if __name__ == "__main__":
    main()
