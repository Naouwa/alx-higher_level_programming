#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in rane(len(row)):
            print("{:d}".format(row[element]),
                    end=" " if element != len(row) -1 else "")
        print()
