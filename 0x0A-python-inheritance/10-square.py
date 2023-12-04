#!/usr/bin/python3

"""Module defines Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the instance"""

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area"""

        return self.__size ** 2
