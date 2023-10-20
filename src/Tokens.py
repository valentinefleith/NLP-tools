from Text import Text


class Tokens:
    def __init__(self, text: Text):
        self.tokens = Tokens.tokenize(text)

    @staticmethod
    def tokenize(text: Text) -> list[str]:
        lemmas = text.get_lemmatized_and_cleaned().split()
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
