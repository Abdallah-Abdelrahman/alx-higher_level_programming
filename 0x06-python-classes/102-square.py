#!/usr/bin/python3


"""This module define a class `Square`.
"""


class Square:
    """Square defines private instance attribute `size`.
    """

    def __init__(self, size=0):
        """Initialize the instance based on size.

        Args:
            size (int): size of the square.

        Raises:
            ValueError: size less than zero
            TypeError: it's not int
        """

        self.size = size

    def __eq__(self, others):
        """ rich comparison ``x == y``."""
        return self.area() == others.area()

    def __nq__(self, others):
        """ rich comparison ``x != y``."""
        return self.area() != others.area()

    def __gt__(self, others):
        """ rich comparison ``x > y``."""
        return self.area() > others.area()

    def __lt__(self, others):
        """ rich comparison ``x < y``."""
        return self.area() < others.area()

    def __ge__(self, others):
        """ rich comparison ``x >= y``."""
        return self.area() >= others.area()

    def __le__(self, others):
        """ rich comparison ``x <= y``."""
        return self.area() <= others.area()


    def area(self):
        """Calculate the area.

        Returns:
            area by raising size to the power 2
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set size"""
        if (type(size) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
