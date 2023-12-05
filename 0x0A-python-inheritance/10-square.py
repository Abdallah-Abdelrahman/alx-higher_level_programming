#!/usr/bin/python3

"""Module defines Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the instance"""

        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        print(self.__size)
        """Return the area"""

        return super().area()
