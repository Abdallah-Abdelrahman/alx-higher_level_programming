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
            TypeError: if value ``not`` int
            ValueError: value <= zero
        """

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
