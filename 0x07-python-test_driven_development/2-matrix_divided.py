#!/usr/bin/python3

"""
A function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix_divided- Function that divides all elemets of a matrix.
    Args:
        matrix: List of lists to be divided.
        div: divisor.
    Returns:
        A matrix with te result of division.
    """
    err00 = 'matrix must be a matrix (list of lists) of integers/floats'
    err01 = 'Each row of the matrix must have the same size'
    ans = []
    if((div is None) or (type(div) != int) and (type(div) != float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (type(matrix) != list):
        raise TypeError(err00)

    for i in range(0, len(matrix)):
        if (type(matrix[i]) != list):
            raise TypeError(err00)
        put_in = []
        for j in range(0, len(matrix[i])):
            if ((type(matrix[i][j]) != int) and (type(matrix[i][j]) != float)):
                raise TypeError(err00)
            if (len(matrix[0]) != len(matrix[i])):
                raise TypeError(err01)
            put_in.append(round((matrix[i][j]) / div, 2))
        ans.append(put_in)
    return (ans)
