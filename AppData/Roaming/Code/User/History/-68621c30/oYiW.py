# WEEK 4 ASSIGNMENTS: FILES, JSON, and CSV

# EXERCISE 1: FILE WRITING
# Write a program that saves your name and city to a text file
# then reads it back and prints it

import tempfile, os
path = tempfile.mktemp(suffix='.txt')
with open(path, 'w') as f:
    f.write("Name: Rhoney\nCity: Manama\n") 
with open(path) as f:
    print(f.read())