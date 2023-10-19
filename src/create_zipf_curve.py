import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import _covariance, linregress

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
    #find_parameters(ranked)


def generate_curve(tokens):
    ranks = np.array([key for key in tokens])
    frequencies = np.array([(tokens[key]) for key in tokens])
    alpha = -find_alpha(ranks, frequencies)[0]
    constant = np.exp(find_alpha(ranks, frequencies)[1])
    plt.plot(ranks, frequencies, label='Donnees')
    plt.plot(ranks, constant * ranks**alpha, label=f'Ajustement : α={alpha:.2f}\n C = {constant:.2f}')
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Loi de Zipf et ajustement par loi de Puissance")
    plt.xlabel("Rang des mots")
    plt.ylabel("Nombre d'occurrences")
    plt.legend()
    plt.show()


def find_alpha(ranks, frequencies):
    log_ranks = np.log(ranks)
    log_freqs = np.log(frequencies)
    slope, intercept, r_value, p_value, std_err = linregress(log_ranks, log_freqs)
    alpha_estimated = -slope
    return alpha_estimated, intercept


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
