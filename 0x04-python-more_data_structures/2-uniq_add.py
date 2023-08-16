#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int_list = set(my_list)
    result = 0
    for number in uniq_int_list:
        result += number
    return result
