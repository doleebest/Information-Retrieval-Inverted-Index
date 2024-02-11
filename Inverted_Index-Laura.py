import os
import re
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def tokenization(text):
    # convert all letters to lowercase
    text = text.lower()

    # convert punctuations to whitespace
    text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)

    # split text into tokens on whitespaces
    tokens = text.split() # default is to split on whitespace
    return tokens

def normalization(tokens):
    p_stem = PorterStemmer()
    tokens_normalized = []
    for token in tokens:
        tokens_normalized.append(p_stem.stem(token))
    return tokens_normalized

test = "I never lived, I never programmed! I didn't want for you to forgive me."

tokens = tokenization(test)
print(tokens)
print(normalization(tokens))