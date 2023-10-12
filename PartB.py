import sys
import re
from PartA import *

file1 = sys.argv[1]
file2 = sys.argv[2]

# print(file1)
# print(file2)

file_1_words = tokenize(file1)
file_2_words = tokenize(file2)

tokens1 = computeWordFrequencies(file_1_words)
tokens2 = computeWordFrequencies(file_2_words)

# print("TOKENS FROM FILE 1: ")
# printTokens(tokens1)
# print("TOKENS FROM FILE 2:")
# printTokens(tokens2)

def commonWords(tokens1, tokens2):
    intersect = tokens1.items() & tokens2.items()
    count = len(intersect)
    for i in sorted(intersect):
        print(i[0], end=" ")
    
    print("\nTotal Common Words:", count)

commonWords(tokens1, tokens2)