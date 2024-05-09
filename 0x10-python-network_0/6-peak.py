#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers
    Args:
        list_of_integers (list): a list of integers
    returns:
        int: peak(s)"""
    list_l = list_of_integers
    if not list_l:
        return None

    length = len(list_l)

    low, high = 0, length - 1
    while low < high:
        mid = (low + high) // 2

        if list_l[mid] < list_l[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_l[low]
