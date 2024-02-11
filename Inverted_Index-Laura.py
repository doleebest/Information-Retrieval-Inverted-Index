import os
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def tokenization(text):
    # convert all letters to lowercase
    text = text.lower()

    # convert punctuations to whitespace
    # \p{P} matches any punctuation character like colon, semicolon, period, etc.
    text = re.sub(r'\p{P}', ' ', text)

    # split text into tokens on whitespaces
    tokens = text.split() # default is to split on whitespace
    return tokens

def normalization(tokens):
    p_stem = PorterStemmer()
    tokens_normalized = []
    for token in tokens:
        tokens_normalized.append(p_stem.stem(token))
    return tokens_normalized

files_path = "C:\Users\laura\OneDrive\Dokumente\ECU\Information retrieval\Project1\Information-Retrieval-Inverted-Index\corpus1"