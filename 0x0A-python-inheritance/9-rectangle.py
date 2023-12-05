#!/usr/bin/python3

"""Module defines Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the instance"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area"""

        return self.__width * self.__height

    def __str__(self):
        """string representaion of the class"""
        return f'[Rectangle] {self.__width}/{self.__height}'
