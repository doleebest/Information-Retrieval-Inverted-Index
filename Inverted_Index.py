import os
import re
import string
from nltk.stem import PorterStemmer

class InvertedIndex:
    def __init__(self):
        self.index = {}

    def tokenize(self, text):
        # Convert all letters to lowercase
        text = text.lower()

        # Replace punctuations with whitespace
        text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', text)

        # Split text into tokens on whitespaces
        tokens = text.split()
        return tokens

    def normalize(self, tokens):
        p_stem = PorterStemmer()
        tokens_normalized = [p_stem.stem(token) for token in tokens]
        return tokens_normalized

    def build_index(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                with open(os.path.join(folder_path, filename), 'r', encoding="utf-8") as file:
                    doc_id = int(os.path.splitext(filename)[0])
                    text = file.read()
                    tokens = self.tokenize(text)
                    normalized_tokens = self.normalize(tokens)
                    for word in normalized_tokens:
                        self.index.setdefault(word, set()).add(doc_id)

    def intersect_search(self, terms):
        docs = set(range(1, num_docs + 1))
        for term in terms:
            docs &= self.single_term_search(term)
        return docs

    def union_search(self, terms):
        docs = set()
        for term in terms:
            docs |= self.single_term_search(term)
        return docs

    def not_search(self, terms):
        return set(range(1, num_docs + 1)) - self.single_term_search(terms[1])

    def single_term_search(self, term):
        matching_docs = set()
        for indexed_term in self.index:
            if term in indexed_term:
                matching_docs |= self.index[indexed_term]
        return matching_docs

    def search(self, query):
        normalized_query = self.normalize(self.tokenize(query))
        if not normalized_query:
            return set()
        elif 'and' in normalized_query:
            return self.intersect_search(normalized_query)
        elif 'or' in normalized_query:
            return self.union_search(normalized_query)
        elif 'not' in normalized_query and len(normalized_query) == 2:
            return self.not_search(normalized_query)
        else:
            results = set(range(1, num_docs + 1))
            for term in normalized_query:
                results &= self.single_term_search(term)
            return results

def user_interface(index):
    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        results = index.search(query)
        if results:
            print("Documents matching the query:")
            for doc_id in sorted(results):
                print(f"Document {doc_id}")
        else:
            print("No documents match the query.")

if __name__ == "__main__":
    index = InvertedIndex()
    folder_path = "./corpus1"  # REPLACE with your folder path here
    num_docs = len([name for name in os.listdir(folder_path) if name.endswith(".txt")])
    index.build_index(folder_path)
    user_interface(index)
