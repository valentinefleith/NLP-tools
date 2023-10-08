import spacy


def lemmatize(text):
    load = spacy.load("fr_core_news_sm", disable=["parser", "ner"])
    doc = load(text)
    final_string = ' '.join(token.lemma_ for token in doc)
    return final_string
