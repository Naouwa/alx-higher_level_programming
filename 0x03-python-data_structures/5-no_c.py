#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for char in new_string:
        if char == 'C' or char == 'c':
            new_string.remove(char)
    return("".join(new_string))
