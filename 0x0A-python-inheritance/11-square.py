#!/usr/bin/python3

"""Module defines Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the instance"""

        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Return the area"""

        return super().area()

    def __str__(self):
        """string representaion of the class"""
        return f'[Square] {self.__size}/{self.__size}'
