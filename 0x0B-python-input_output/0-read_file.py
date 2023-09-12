#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """ a function that reads a text file, and prints it to the stdout"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
