import sys
import re

filename = sys.argv[1]

def tokenize(filename):
    tokens = []
    with open(filename, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            # Use regular expression to match English words
            english_words = re.findall(r'\b[a-zA-Z]+\b', line)
            tokens.extend(word.lower() for word in english_words)
        print("Tokens: ", tokens)

tokenize(filename)
