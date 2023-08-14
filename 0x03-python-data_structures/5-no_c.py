#!/usr/bin/python3
def no_c(my_string):
    new_string = [a for a in my_string if a != 'c' and a != 'C']
    return("".join(new_string))
