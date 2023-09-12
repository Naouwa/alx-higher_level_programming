#!/usr/bin/python3
"""Read file module"""


def append_write(filename="", text=""):
    """
    It appends a string at the end of a text file, 
    and returns the number of charracters added
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
