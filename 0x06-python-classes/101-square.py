#!/usr/bin/python3


"""This module define a class `Square`."""


class Square:
    """Square defines private instance attribute `size`."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the instance based on size.

        Args:
            size (int): size of the square.
            position (tuple): tuple of 2 positive int

        Raises:
            ValueError: size less than zero.
            TypeError: size is not int or position is not tuple
                of 2 positive int.
        """

        self.size = size
        self.position = position

    def my_print(self):
        """Print the sqaure."""

        if (not self.__size):
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range((self.__position[0])):
                print(' ', end='')
            for _ in range(self.__size):
                print('#', end='')
            print()

    def area(self):
        """Calculate the area.

        Returns:
            area by raising size to the power 2
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get size"""
        return self.__size

    @property
    def position(self):
        """Get position."""
        return self.__position

    @position.setter
    def position(self, position):
        """Set position."""
        if not position or not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        _len = len(position)
        if (not _len or _len != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        x, y = position
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    @size.setter
    def size(self, size):
        """Set size"""
        if (type(size) is not int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def __repr__(self):
        """Print Sqaure"""
        if (not self.__size):
            print()
            return ''
        for _ in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for _ in range((self.__position[0])):
                print(' ', end='')
            for _ in range(self.__size):
                print('#', end='')
            print(end=('', '\n')[i < self.__size - 1])
        return ''
