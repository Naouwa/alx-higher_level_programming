#!/usr/bin/python3
"""File insertion module"""


def append_after(filename="", search_string="", new_string=""):
    """
    It inserts a line of text to a file,
    after each line containong a specific string
    """
    lines = []
    with open(filename, mode="r", encoding="UTF-8") as f:
        lines = f.readlines()
        letter = 0
        while letter < len(lines):
            if search_string in lines[letter]:
                lines[letter:letter + 1] = [lines[letter], new_string]
                letter += 1
            letter += 1
    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(lines)
