#!/usr/bin/python3
'''
a function yhat reads a file
'''

def read_file(filename=""):
    '''reads a text file (UTF8) and prints it to stdout
    Returns nothing
    '''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
