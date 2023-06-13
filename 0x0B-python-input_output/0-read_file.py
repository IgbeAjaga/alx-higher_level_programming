#!/usr/bin/python3
"""
Definesthe reading of files
"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) & prints it to stdout"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
