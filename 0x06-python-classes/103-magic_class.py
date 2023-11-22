#!/usr/bin/python3
import math


""" module defines ``MagicClass``"""


class MagicClass:
    """ magic"""
    def __init__(self, radius):
        """Initialize instance"""
        self.__radius = 0
        if (type(radius) is not int or type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ circumference."""
        return math.pi * 2 * self.__radius
