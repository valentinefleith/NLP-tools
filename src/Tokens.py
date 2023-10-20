from Text import Text


class Tokens:
    def __init__(self, text: Text):
        self.tokens = Tokens.tokenize(text)
        self.lemmas = text.get_lemmatized_and_cleaned().split()
        self.occ_dict = self.get_occ_dict()
        self.occ_dict_without_stopwords = self.remove_empty_words()

    @staticmethod
    def tokenize(text: Text) -> list[str]:
        lemmas = text.get_raw_cleaned().split()
        tokens = Tokens.split_apostrophes(lemmas)
        return tokens

    @staticmethod
    def split_apostrophes(words: list[str]) -> list[str]:
        # apostrophe = "'"
        apostrophe = "’"
        apostrophes = []
        indices = []
        for index, word in enumerate(words):
            if apostrophe in word:
                first, second, *_ = word.split(apostrophe)
                apostrophes.append(first + apostrophe)
                apostrophes.append(second)
                indices.append(index)
        indices.reverse()
        for i in indices:
            words.pop(i)
        return words + apostrophes

    def get_occ_dict(self):
        occurrences_dict = {}
        for element in self.tokens:
            if element in occurrences_dict:
                occurrences_dict[element] += 1
            else:
                occurrences_dict[element] = 1
        return Tokens.sort_dict(occurrences_dict)

    def remove_empty_words(self):
        path = "aux/stop_words.txt"
        with open(path, "r") as empty_words:
            stop_words = empty_words.read()
            new_dict = {key: self.occ_dict[key] for key in self.occ_dict if key not in stop_words}
        return new_dict

    @staticmethod
    def sort_dict(dictionary):
        sorted_keys = sorted(dictionary, key=dictionary.get)
        sorted_dict = {key: dictionary[key] for key in sorted_keys}
        return sorted_dict
