import sys

import occurrences_dict
#from create_zipf_curve import generate_curve, rebuild_dictionary


def main():
    """
    This module generates a Zipf graph from a text file
    -----------
    Argument : path to text file
    Output : Zipf's curve
    """
    if len(sys.argv) != 2:
        sys.exit("Usage : py stats.py /path/to/file.txt")

    tokens = occurrences_dict.create_dict(sys.argv[1])
    tokens = occurrences_dict.sort_dict(tokens)
    ranked = rebuild_dictionary(rank_words(tokens))
    generate_curve(ranked)


def find_relative_frequency(tokens):
    """
    Given a dictionary of word:occurrence
    finds frequency of every word.
    Output : dictionary containing word:frequency
    """
    NUMBER_OF_TOKENS = len(tokens)
    frequencies = {}
    for key in tokens:
        frequency = tokens[key] / NUMBER_OF_TOKENS
        frequencies[key] = frequency
        # print(f"Frequence du mot {key} : {frequency}%")
    return frequencies

if __name__ == "__main__":
    main()
