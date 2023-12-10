#!/usr/bin/python3
"""Module defines Square class"""

from rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from `Rectangle`"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance.

        Args:
            size: size of the `Square`
            x: horizental padding
            y: vertical padding
            id: identity of the class

        Raises:
            TypeError: if input is not integer
            ValueError: if `size` less than or equal to zero,
                or `x` or `y` less than zero
        """

        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    def update(self, *args, **kwargs):
        """Updates instance attributes

        Args:
            *args: tuple of variable arguments
            **kwargs: dictionary of keyword arguments

        Note:
            *args is the list of arguments - no-keyworded arguments:
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 3rd argument should be the x attribute
            - 4th argument should be the y attribute
        """

        attrs = ['id', 'size', 'x', 'y']

        for i, arg in enumerate(args):
            setattr(self, attrs[i], arg)
            if arg == 'size':
                setattr(self, 'width', arg)
                setattr(self, 'height', arg)

        if not len(args):
            for k, v in kwargs.items():
                setattr(self, k, v)
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        return {k: getattr(self, k) for k in ['id', 'x', 'size', 'y']}

    @property
    def size(self):
        """Getter for size(width and height)"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for size(width and height)"""

        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size
        self.__size = size

    def __str__(self):
        """string representation of Square"""

        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)
