#!/usr/bin/python3
"""program that prints the ASCII alphabet, in lowercase, not followed by\n"""

for index in range(97, 123):
    if (chr(index) != 'e' and chr(index) != 'q'):
        print("{:c}".format(index), end='')
