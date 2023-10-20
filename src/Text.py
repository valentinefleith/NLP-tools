import spacy


class Text:
    def __init__(self, path: str):
        self.raw = Text.load_file(path)

    def get_lemmas(self) -> str:
        raw_text = self.raw
        load = spacy.load("fr_core_news_sm", disable=["parser", "ner"])
        doc = load(raw_text)
        lemmatized = " ".join(token.lemma_ for token in doc)
        return lemmatized

    def get_cleaned_lemmas(self) -> str:
        cleaned = ""
        for char in self.get_lemmas():
            if char not in "?!():;.,«»–¬—*":
                cleaned += char
        return cleaned.replace("\n", " ").lower()

    @staticmethod
    def load_file(path: str) -> str:
        with open(path, "r") as text:
            return text.read()
