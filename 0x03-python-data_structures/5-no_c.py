#!/usr/bin/python3
def no_c(my_string):
    n_string = list(my_string)
    for character in n_string:
        if character == 'C' or character == 'c':
            n_string.remove(character)
    return("".join(n_string))
