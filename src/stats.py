import argparse

from create_dict_tokens import create_dict


def main():
    parser = argparse.ArgumentParser(
                    prog="py tokenization.py",
                    description='Tokenize a text file.')
    parser.add_argument('filename')
    args = parser.parse_args()
    tokens = create_dict(args.filename)
    frequencies = find_relative_frequency(tokens)
    print(frequencies)


def find_relative_frequency(tokens):
    NUMBER_OF_TOKENS = len(tokens)
    frequencies = {}
    for key in tokens:
        frequency = round(tokens[key] * 100 / NUMBER_OF_TOKENS, 2)
        frequencies[key] = frequency
        #print(f"Frequence du mot {key} : {frequency}%")
    return frequencies



if __name__ == "__main__":
    main()
