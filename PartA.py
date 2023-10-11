import sys
import re

filename = sys.argv[1]

def tokenize(filename):
    tokens = []
    with open(filename, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            # Use regular expression to split text by non-alphanumeric characters
            words = re.findall(r'\w+', line)
            for word in words:
                tokens.append(word.lower())
        print("Tokens: ", tokens)

tokenize(filename)
