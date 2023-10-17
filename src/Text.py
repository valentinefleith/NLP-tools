import spacy


class Text:
    def __init__(self, path):
        self.raw = Text.load_file(path)

    def get_lemmas(self):
        raw_text = self.raw
        load = spacy.load("fr_core_news_sm", disable=["parser", "ner"])
        doc = load(raw_text)
        lemmatized = ' '.join(token.lemma_ for token in doc)
        return lemmatized

    def get_cleaned_lemmas(self):
        cleaned = ""
        for char in self.get_lemmas():
            #if char == "\n":
               #cleaned += " "
            if char not in "?!():;.,«»–¬—*":
                cleaned += char
        return cleaned.replace("\n", " ").lower()

    @staticmethod
    def load_file(path):
        with open(path, "r") as text:
            return text.read()
