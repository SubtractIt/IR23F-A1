# Imports the sys and re libraries to access command line arguments and PartA.py to access tokenizer methods
import sys
import re
from PartA import *

print("\nPart B: Intersection of Two Files\n")

# Sets filenames to be the files passed in through the command line
file1 = sys.argv[1]
file2 = sys.argv[2]

# testing filenames
# print(file1)
# print(file2)

# calls tokenize method and passes in the new file names, stores values ina list of words
file_1_words = tokenize(file1)
file_2_words = tokenize(file2)

# uses PartA method to compute the total word frequencies from the files
tokens1 = computeWordFrequencies(file_1_words)
tokens2 = computeWordFrequencies(file_2_words)

# print("TOKENS FROM FILE 1: ")
# printTokens(tokens1)
# print("TOKENS FROM FILE 2:")
# printTokens(tokens2)

# commonWords - takes two dictionaries of tokens and uses the set union
# Complexity - O(n + m + nlogn) - n represents the size of tokens1 and m represents the size of tokens2
# Must iterate through each of the tokens and find intersections using the & operator, then sort the intersection in O(nlogn) and print the count
def commonWords(tokens1, tokens2):
    # performs a set intersection of the items of the two files using the &
    intersect = tokens1.items() & tokens2.items()

    # sets the count to be equal to the length of the intersection - number of common tokens
    count = len(intersect)

    # sorts the intersected tokens and prints the words that are common to both files
    for i in sorted(intersect):
        print(i[0], end=" ")
    
    print("\nTotal Common Words:", count)

# function call
commonWords(tokens1, tokens2)