import sys

filename = sys.argv[1]

def tokenize(filename):
    with open(filename,'r') as data_file:
        for line in data_file:
            data = line.split()
            # print(data)
        print(data_file.read())

tokenize(filename)