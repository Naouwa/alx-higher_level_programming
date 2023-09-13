#!/usr/bin/python3
"""The pascal's triangle of n"""


def pascal_triangle(n):
    """It returns a list of lists of integers representing"""
    if n <= 0:
        return []

    lists = [[1 for tri in range(row + 1)] for row in range(n)]
    for n in range(n):
        for row in range(n - 1):
            lists[n][row + 1] = sum(lists[n - 1][row:row + 2])
    return lists
