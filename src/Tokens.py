from typing import List, Dict

from Text import Text


class Tokens:
    """
    A class to represent tokens from a text.

    Attributes
    ----------
    tokens : lst[str]
        list of all the words of the text
    lemmas : lst[str]
        list of all the lemmas of the text
    occ_dict : dict{str: int}
        keys are the words, values the number of occurrences
    occ_dict_without_stopwords : dict{str: int}
        keys are the words, values the number of occurrences
    """
    def __init__(self, text: Text):
        self.tokens = Tokens.tokenize(text)
        self.lemmas = text.get_lemmatized_and_cleaned().split()

    @staticmethod
    def tokenize(text: Text) -> List[str]:
        """Takes in a text, returns a list of all its words."""
        tokens = text.get_raw_cleaned().split()
        return tokens

    def get_occ_dict(self) -> Dict[str, int]:
        return Tokens.create_occ_dict(self.tokens)

    def get_occ_dict_without_stopwords(self, path_to_stopwords="aux/stop_words.txt") -> Dict[str, int]:
        """From a dict {word: occurences}, removes stop-words"""
        with open(path_to_stopwords, "r") as empty_words:
            stop_words = empty_words.read()
            occ_dict = self.get_occ_dict()
            new_dict = {key: occ_dict[key] for key in occ_dict if key not in stop_words}
        return new_dict

    def get_ngrams(self, n: int) -> List[List[str]]:
        tokens = self.tokens
        ngrams = []
        for i in range(len(tokens) - n + 1):
            ngrams.append([tokens[i + j] for j in range(n)])
        return ngrams


    @staticmethod
    def create_occ_dict(tokens: List[str]) -> Dict[str, int]:
        """Takes in a list of tokens, returns a dict {word: occurences}"""
        occurrences_dict = {}
        for element in tokens:
            if element in occurrences_dict:
                occurrences_dict[element] += 1
            else:
                occurrences_dict[element] = 1
        return Tokens.sort_dict(occurrences_dict)

    @staticmethod
    def sort_dict(dictionary):
        """Takes in a dict, returns the dict sorted in value desc order"""
        sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
        sorted_dict = {key: dictionary[key] for key in sorted_keys}
        return sorted_dict
