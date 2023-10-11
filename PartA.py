import sys
import re

filename = sys.argv[1]

def tokenize(filename):
    tokens = []
    with open(filename, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            words = re.findall(r'\b[a-zA-Z0-9]+\b', line)
            tokens.extend(word.lower() for word in words)
        # print("Tokens: ", tokens)

    return tokens


def computeWordFrequencies(tokens):
    dict = {}

    for token in tokens:
        if token in dict:
            dict[token] = dict[token] + 1
        else:
            dict[token] = 1

    # print("Token Dictionary: ", dict)

    return dict

def printTokens(token_dict):
    sorted_dict = sorted(token_dict.items(), key=lambda x:x[1], reverse=True)
    for key, value in sorted_dict:
        print(f"{key} - {value}")

words = tokenize(filename)
# print(words)
tokens = computeWordFrequencies(words)
printTokens(tokens)

