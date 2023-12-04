#!/usr/bin/python3
"""Module defines Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the instance"""
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
