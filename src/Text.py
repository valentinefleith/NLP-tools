import spacy


class Text:
    PUNCTUATION = "?!():;.,«»–¬—*"

    def __init__(self, path: str):
        self.raw = Text.load_file(path)
        self.lemmas = Text.lemmatize(self.raw)

    @staticmethod
    def lemmatize(raw_text: str) -> str:
        load = spacy.load("fr_core_news_sm", disable=["parser", "ner"])
        doc = load(raw_text)
        lemmatized = " ".join(token.lemma_ for token in doc)
        return lemmatized

    def get_lemmatized_and_cleaned(self) -> str:
        return Text.clean(self.lemmas)

    def get_raw_cleaned(self) -> str:
        return Text.clean(self.raw)

    @classmethod
    def clean(cls, string: str) -> str:
        cleaned = ""
        for char in string:
            if char not in Text.PUNCTUATION:
                cleaned += char
        return cleaned.replace("\n", " ").lower()

    @staticmethod
    def load_file(path: str) -> str:
        with open(path, "r") as text:
            return text.read()
