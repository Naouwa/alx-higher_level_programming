#!/usr/bin/python3
"""Read file module"""


def write_file(filename="", text=""):
    """
    It writes a string to a text file and returns the of characters written
    """

    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))

    """charCount = len(text)

    return charCount"""
