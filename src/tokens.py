from text import Text


class Tokens:
    def __init__(self, text):
        self.tokens = text.get_cleaned_lemmas().get_tokens()

    def get_tokens(self, text):
        tokens = text.split()
        tokens += self.split_apostrophes(text)
        return tokens

    def split_apostrophes(self, text):
        # apostrophe = "'"
        apostrophe = "’"
        apostrophes = []
        indices = []
        for index, word in enumerate(text):
            if apostrophe in word:
                temp = word.split(apostrophe)
                apostrophes.append(temp[0] + apostrophe)
                apostrophes.append(temp[1])
                indices.append(index)
        indices.reverse()
        for i in indices:
            text.pop(i)
        return apostrophes
