import argparse

from create_dict_tokens import create_dict


def main():
    parser = argparse.ArgumentParser(
                    prog="py tokenization.py",
                    description='Tokenize a text file.')
    parser.add_argument('filename')
    args = parser.parse_args()
    tokens = create_dict(args.filename)
    find_relative_frequency(tokens)
    print(len(tokens))


def find_relative_frequency(tokens):
    NUMBER_OF_TOKENS = len(tokens)
    for key in tokens:
        frequency = round(tokens[key] * 100 / NUMBER_OF_TOKENS, 2)
        print(f"Frequence du mot {key} : {frequency}%")


if __name__ == "__main__":
    main()
