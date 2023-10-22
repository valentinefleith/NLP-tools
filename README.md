# My tools for NLP in Python

## Requirements

-`spacy`, especially `fr_core_news_sm`

```
pip install spacy
python3 -m spacy download ft_core_news_sm
```

## Modules

- [`Text.py`](/src/Text.py) : load, clean, and lemmatize a text.
- [`Tokens.py`](/src/Tokens.py) : tokenize, count words, remove empty words from a text.

## Todo

- Attribute in Tokens for pos-tagging the corpus
- N-grams generators
- Bag of words
