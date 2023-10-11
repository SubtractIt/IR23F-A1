import sys

filename = sys.argv[1]

def tokenize(filename):
    tokens = []
    with open(filename,'r', encoding='utf-8') as data_file:
        for line in data_file:
            data = line.split()
            tokens.extend(word.lower() for word in data)  # Convert each word to lowercase
        print("Tokens: ", tokens)

tokenize(filename)