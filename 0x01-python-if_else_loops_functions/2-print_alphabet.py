#!/usr/bin/python3
"""a program that prints the ASCII alphabet, in lowercase, not followed by \n"""
for i in range(ord('a'), ord('z') + 1):
    print("{:s}".format(chr(i)), end="")

