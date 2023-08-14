#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return (None)

    largest_i = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > largest_i:
            largest_i = my_list[i]
    return (largest_i)
