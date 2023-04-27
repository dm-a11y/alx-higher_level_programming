#!/usr/bin/python3
""" a program that prints the ASCII alphabet, in lowercase, not followed by a new line."""

for index in range(97, 123):
    if (chr(index) != 'e' and chr(index) != 'q'):
        print("{:c}".format(index), end='')
