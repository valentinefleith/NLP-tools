import argparse

import create_dict_tokens


def main():
    parser = argparse.ArgumentParser(
                    prog="py tokenization.py",
                    description='Tokenize a text file.')
    parser.add_argument('filename')
    parser.add_argument('top_x_words', nargs="?")
    args = parser.parse_args()
    tokens = create_dict_tokens.create_dict(args.filename)
    tokens = create_dict_tokens.sort_dict(create_dict_tokens.remove_empty_words(tokens))
    frequencies = find_relative_frequency(tokens)
    if args.top_x_words:
        print_x_first_frequencies(frequencies, int(args.top_x_words))
    else:
        print(frequencies)


def find_relative_frequency(tokens):
    NUMBER_OF_TOKENS = len(tokens)
    frequencies = {}
    for key in tokens:
        frequency = round(tokens[key] * 100 / NUMBER_OF_TOKENS, 2)
        frequencies[key] = frequency
        #print(f"Frequence du mot {key} : {frequency}%")
    return frequencies

def print_x_first_frequencies(frequencies, number):
    counter = 1
    while counter <= number:
        i = -counter
        key = list(frequencies)[i]
        print(f"{counter}) Frequence du mot {key} : {frequencies[key]}")
        counter += 1



if __name__ == "__main__":
    main()
