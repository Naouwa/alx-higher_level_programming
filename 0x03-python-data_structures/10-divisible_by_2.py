#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multi_list = []
    for integer in my_list:
        if integer % 2 == 0:
            multi_list.append(True)
        else:
            multi_list.append(False)
    return multi_list
