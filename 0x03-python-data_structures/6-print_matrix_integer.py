#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(len(row)):
            print("{:d}".format(row[element]),
                    end=" " if element < row[-1] or element > row[-1] else "")
            print()
