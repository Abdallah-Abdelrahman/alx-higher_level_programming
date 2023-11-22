#!/usr/bin/python3

""" module defines ``MagicClass``"""


class MagicClass:
    """ magic"""
    def __init__(self, radius=0):
        """Initialize instance"""
        self.__radius = 0
        if (type(radius) not in (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area."""
        return self.__radius ** 2 * __import__('math').pi

    def circumference(self):
        """ circumference."""
        return __import__('math').pi * 2 * self.__radius
