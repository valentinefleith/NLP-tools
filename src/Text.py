import spacy


class Text:
    def __init__(self, path):
        self.raw = Text.load_file(path)

    def get_lemmatized(self):
        raw_text = self.raw
        load = spacy.load("fr_core_news_sm", disable=["parser", "ner"])
        doc = load(raw_text)
        lemmatized = ' '.join(token.lemma_ for token in doc)
        return lemmatized

    def get_cleaned(self):
        cleaned = ""
        for char in self.get_lemmatized():
            if char == "\n":
                cleaned += " "
            if char not in "?!():;.,«»–¬—*":
                cleaned += char.lower()
        return cleaned

    @staticmethod
    def load_file(path):
        with open(path, "r") as text:
            return text.read()
