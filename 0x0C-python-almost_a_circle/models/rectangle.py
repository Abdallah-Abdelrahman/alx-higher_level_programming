#!/usr/bin/python3
"""Module defines `Rectangle` class."""

from base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the instance.

        Args:
            width(int): width of Rectangle
            height(int): height of Rectangle
            x: horizental padding
            y: vertical padding
            id: identity of the class

        Raises:
            TypeError: if input is not integer
            ValueError: if `width` or `height` less than or equal to zero,
                or `x` or `y` less than zero
        """

        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        """Return the area"""

        return self.__width * self.__height

    def update(self, *args, **kwargs):
        """Updates instance attributes

        Args:
            *args: tuple of variable arguments
            **kwargs: dictionary of keyword arguments
        """

        attrs = ['id', 'width', 'height', 'x', 'y']

        for i, arg in enumerate(args):
            setattr(self, attrs[i], arg)

        if not len(args):
            for k, v in kwargs.items():
                setattr(self, k, v)

    def display(self):
        """Outputs Rectangle instance to stdout"""

        print('\n' * self.__y + '\n'.join
              ([self.__x * ' ' + '#'
                * self.__width for _ in range(self.__height)]))

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        
        return {k: getattr(self, k) for k in ['x', 'y', 'id', 'height', 'width']}

    def __str__(self):
        """string representation of Rectangle"""

        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""

        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""

        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height
