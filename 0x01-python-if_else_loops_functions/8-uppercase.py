#!/usr/bin/python3
"""a function that prints a string in uppercase followed by a new line."""

def uppercase(str):
    for i in range(len(str)):
        upper = str[i]
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            upper = chr(ord(str[i]) - 32)
        print("{}".format(upper), end='')
    print()
