#!/usr/bin/python3

"""Module defines `BaseGeometry` class"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """Raises an error"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """"validates value

        Args:
            value(int): value
            name(str): name
        Raises:
            TypeError: value is not int
            ValueError: value <= zero
        """

        if not isinstance(value, int):
            raise TypeError('%s must be an integer' % name)
        if value <= 0:
            raise ValueError('%s must be greater than 0' % name)
