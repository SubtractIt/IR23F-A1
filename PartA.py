# Imports the sys and re libraries to access command line arguments and
# parsing capabilities
import sys
import re

# sets filename to the first argument passed through to the command line
filename = sys.argv[1]

# Tokenize - takes parameter filename, which is obtained from cmd line
# Parses through every line in the file and extrapolates all tokens that are
# alphanumeric and non-puncutation - returns list of tokens

# Complexity - O(n) - This function runs in linear time based on the size of the input file (n). 
# This is because it iterates through each line in the file and uses a 'regexp' (regular expression) to parse through the file and
# return words only satisfying the boundary constraint in place (in this case, only alphanumerics)
def tokenize(filename):

    # creates empty list of tokens
    tokens = []

    # opens file in utf-8 format and iterates through each line in the file
    with open(filename, 'r', encoding='utf-8') as data_file:

        for line in data_file:

            # uses the findall() function in order to only obtain alphanumerics 
            words = re.findall(r'\b[a-zA-Z0-9]+\b', line)

            # uses extend() function to add the lowercase word into the list of tokens
            tokens.extend(word.lower() for word in words)

        # print("Tokens: ", tokens)

    # print("TOKENS: ", len(tokens))
    return tokens

# computeWordFrequencies - iterates through the tokens list and calculates frequency of each token
# Complexity - O(n) - This function runs in linear time to the size of the list of tokens it receives as an argument, where n = len(tokens), 
# as the function iterates through each value in this 'tokens' list
def computeWordFrequencies(tokens):

    # create empty dictionary - key: token, value: token count
    dict = {}

    # iterates through the tokens list

    for token in tokens:

        # if the token is already in our dictionary, then increment the value of that token
        if token in dict:
            dict[token] = dict[token] + 1

        # else, set the value to 1 as this is the first occurence
        else:
            dict[token] = 1

    # print("Token Dictionary: ", dict)
    
    return dict

# printTokens - receives dictionary as a parameter and sorts them in descending value count order
# Complexity - O(nlogn) - as this method takes a dictionary of tokens and iterates through the dictionary after sorting, printing each (k, v) pair
def printTokens(token_dict):
    # uses the sorted function with a lambda key in order to sort by descending value count
    sorted_dict = sorted(token_dict.items(), key=lambda x:x[1], reverse=True)

    # prints each key value pair separated by a '-'
    for key, value in sorted_dict:
        print(f"{key} - {value}")
    
    # prints the number of tokens
    num_tokens = len(sorted_dict)
    print(f"Number of Unique Tokens: {num_tokens}")

# Runs our code
def main():
    print("\nPart A: Word Frequencies\n")
    words = tokenize(filename)
    # print(words)
    tokens = computeWordFrequencies(words)
    printTokens(tokens)

if __name__ == "__main__":
    main()