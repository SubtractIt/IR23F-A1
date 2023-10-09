import sys

filename = sys.argv[1]

file = open(filename, "r")
print(file.read())
file.close()

