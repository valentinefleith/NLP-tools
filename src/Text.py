import spacy


class Text:
    def __init__(self):
        pass

    def get_raw(self, path):
        with open(path, "r") as text:
            return text.read()

    def get_lemmatized(self, path):
        raw_text = self.get_raw(path)
        load = spacy.load("fr_core_news_sm", disable=["parser", "ner"])
        doc = load(raw_text)
        lemmatized = ' '.join(token.lemma_ for token in doc)
        return lemmatized

    def get_cleaned(self, lemmatized):
        cleaned = ""
        for char in lemmatized:
            if char == "\n":
                cleaned += " "
            if char not in "?!():;.,«»–¬—*":
                cleaned += char.lower()
        return cleaned
