import math
import sys
import numpy as np
import matplotlib.pyplot as plt

from occurrences_dict import create_dict, sort_dict


def main():
    """
    This module generates a Zipf graph from a text file
    -----------
    Argument : path to text file
    Output : Zipf's curve
    """
    if len(sys.argv) != 2:
        sys.exit("Usage : py stats.py /path/to/file.txt")

    tokens = sort_dict(create_dict(sys.argv[1]))
    ranked = rebuild_dictionary(rank_words(tokens))
    generate_curve(ranked)


def generate_curve(tokens):
    x = np.array([math.log(key) for key in tokens])
    y = np.array([math.log(tokens[key]) for key in tokens])

    plt.plot(x, y)
    plt.title("Loi de Zipf")
    plt.xlabel("Logarithme du rangs des mots")
    plt.ylabel("Logarithme du nombre d'occurrences")
    plt.show()


def rank_words(dictionary):
    """
    Given a dictionary of word:occurrence or word:frequency,
    ranks the words in desc order.
    Output : dictionary containing rank:occurrence / rank:frequency
    """
    rank = 1
    ranked = {}
    for key in dictionary:
        i = -rank
        ranked[rank] = dictionary[list(dictionary)[i]]
        rank += 1
    return ranked


def rebuild_dictionary(tokens):
    """
    Given a dictionary of rank:occurrence,
    groups words if they have the same number of occurrences.
    Output : dictionary containing rank:occurrence where occurrence is unique
    """
    rebuilt_dict = {}
    current_key = 1
    for key in tokens:
        if current_key == 1 or tokens[current_key] != tokens[key]:
            current_key = key
            rebuilt_dict[current_key] = tokens[key]
    sorted_dict = {}
    start = 1
    for key in rebuilt_dict:
        sorted_dict[start] = rebuilt_dict[key]
        start += 1
    return sorted_dict


if __name__ == "__main__":
    main()
