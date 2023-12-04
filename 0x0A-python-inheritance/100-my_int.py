#!/usr/bin/python3

"""Module defines MyInt class"""


class MyInt(int):
    """inherits from int"""

    def __init__(self, n):
        """Initialize the instance"""
        self.__n = n

    def __eq__(self, other):
        """Overload `!=` operator """
        return self.__n != other

    def __ne__(self, other):
        """Overload `==` operator"""
        return self.__n == other

    def __str__(self):
        return str(self.__n)
