# My tools for NLP in Python

## Requirements

`spacy`, especially `fr_core_news_sm`

```
pip install spacy
python3 -m spacy download ft_core_news_sm
```

NB : only the lemmatization part will use `spacy`.

## Modules

### Classes

- [`Text.py`](/src/Text.py) : load, clean, and lemmatize a text.
- [`Tokens.py`](/src/Tokens.py) : tokenize, count words, remove empty words, get n-grams from a text.

### Files

- [`stop_words.txt`](/aux/stop_words.txt) : list of stop-words used to remove empty words
- [`texts`](/texts) : some texts to try the tools (NB : Rousseau's still not working, will be soon)

## Todo

- Create token class so that tokens are list of token (attributes : pos, lemmas, etc.)
- Bag of words
- Freq ranked dict
