import re
import string
from nltk.stem import PorterStemmer

def tokenize(text):
    # Convert all letters to lowercase
    text = text.lower()

    # Replace punctuations with whitespace
    text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)

    # Split text into tokens on whitespaces
    tokens = text.split()
    return tokens

def normalize(tokens):
    p_stem = PorterStemmer()
    tokens_normalized = [p_stem.stem(token) for token in tokens]
    return tokens_normalized

test = "My code is programmed to search words."

tokens = tokenize(test)
print(tokens)
print(normalize(tokens))
