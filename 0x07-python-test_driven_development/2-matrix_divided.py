#!/usr/bin/python3

"""This module defines ``matrix_divided`` function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Each row of the matrix must of the same size,
    all elements of the matrix should be divided by ``div``,
    rounded to 2 decimal places.

    Args:
        matrix: a list of list of int or float
        div: a number int or float

    Returns:
        new matrix

    Raises:
        TypeError: if matrix isn't composed of a list of int or float
            if each row size are different
            `div` is not a number (int or float).
        ZeroDivisionError: `div` equals to zero.
    """
    err = 'matrix must be a matrix (list of lists) of integers/floats'

    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if (div == 0):
        raise ZeroDivisionError('division by zero')
    if not matrix or not isinstance(matrix, list):
        raise TypeError(err)

    for i, row in enumerate(matrix):
        if i and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError('Each row of the matrix must have the same size')
        if not isinstance(row, list):
            raise TypeError(err)
        new_matrix.append([])
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(err)
            new_matrix[i].append(round(col / div, 2))

    return new_matrix
