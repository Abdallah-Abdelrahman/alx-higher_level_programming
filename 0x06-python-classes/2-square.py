#!/usr/bin/python3

"""This module define a class `Square`.
"""


class Square:
    """Square defines private instance attribute `size`.
    """
    def __init__(self, size=0):
        """Initialize the instance based on size.

        if size less than zero `ValueError` will be raised
        if it's not int `TypeError` will be raised.

        Args:
            size (int): size of the square.
        """
        if (type(size) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')

        self.__size = size
