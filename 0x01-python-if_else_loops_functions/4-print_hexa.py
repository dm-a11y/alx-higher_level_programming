#!/usr/bin/python3
"""a program that prints all numbers from 0 to 98 in decimal and in hex"""

for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
