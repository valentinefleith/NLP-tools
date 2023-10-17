import spacy


class Text:
    def __init__(self, path):
        self.raw = Text.load_file(path)
    
    @staticmethod
    def load_file(path):
        with open(path, "r") as text:
            return text.read()

    def get_lemmatized(self):
        raw_text = self.raw
        load = spacy.load("fr_core_news_sm", disable=["parser", "ner"])
        doc = load(raw_text)
        lemmatized = ' '.join(token.lemma_ for token in doc)
        return lemmatized

    @staticmethod
    def get_cleaned(lemmatized):
        cleaned = ""
        for char in lemmatized:
            if char == "\n":
                cleaned += " "
            if char not in "?!():;.,«»–¬—*":
                cleaned += char.lower()
        return cleaned
