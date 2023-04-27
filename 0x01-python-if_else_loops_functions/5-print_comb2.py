#!/usr/bin/python3
"""a program that prints numbers from 0 to 99."""

for i in range(0, 99):
    print("{0:02d}".format(i), end=", ")
print("{:d}".format(99))
