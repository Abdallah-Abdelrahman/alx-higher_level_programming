#!/usr/bin/python3

"""This module define a class `Square`.
"""


class Square:
    """Square defines private instance attr.
    """
    def __init__(self, size):
        """Initialize the instance based on size.

        Args:
            size: size of the square
        """
        self.__size = size
