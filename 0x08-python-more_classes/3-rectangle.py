#!/usr/bin/python3

"""Define class Rectangle"""


class Rectangle:
    """Definition"""

    def __init__(self, width=0, height=0):
        """Initialize the instance

        Args:
            width: integer
            height: integer

        Raises:
            TypeError: width or height not integer
            ValueError: width or height < zero
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set width"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set height"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Calculate the distance inside"""
        return self.width * self.height

    def perimeter(self):
        """The distance all the way around the outside"""
        return 2 * (self.width + self.height)\
            if self.width and self.height\
            else 0

    def __str__(self):
        """Print ``Rectangle``"""
        _str = ''
        if (not self.width or not self.height):
            return _str
        for i in range(self.height):
            _str += '#' * self.width + ('', '\n')[i < self.height - 1]
        return _str
