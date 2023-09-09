#!/usr/bin/python3
def matrix_divide(matrix, div):
    """Devides all the elements of a matrix
        args:
            matrix: the elements to divide by div
            div: the devision number

        Raises:
            TypeError: if matrix is not a list of lists of int or float.
            TypeError: if each row of matrix is not of same size.
            TypeError: if div is neither an int nor float
            ZeroDivisionError: if div is zero

        return:  a new matrix with elements rounded to 2 decimal places.
    """
    errorM = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(errorM)
    if not isinstance(matrix, list):
        raise TypeError(errorM)
    for elemets in matrix:
        if not isinstance(elements, list):
            raise TypeError(errorM)
        for itm in elements:
            if not isinstance(itm, int) and not isinstance(itm, float):
                raise TypeError(errorM)
    for elements in matrix:
        if len(elements) == 0:
            raise TypeError(errorM)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(elements) == len(matrix[0]) for elements in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(itm / div, 2) for itm in elemets] for elements in matrix]
