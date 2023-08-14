#!/usr/bin/python3
def no_c(my_string):
    new_string = [a for a in my_string if a != 'C' and a != 'c']
    return("".join(new_string))
