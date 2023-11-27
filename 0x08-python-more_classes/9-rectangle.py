#!/usr/bin/python3

"""Define class Rectangle"""


class Rectangle:
    """Definition.

    Attributes:
        number_of_instances: integer
        print_symbol: symbole to print
    """

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare 2 instances.

        Args:
            rect_1: instance
            rect_2: instance

        Raises:
            TypeError: if rect_1 or rect_2 not instance of ``Rectangle``

        Returns:
            biggest rectangle based on the area,
                rect_1 if both have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance.

        where width == height == size
        """

        return cls(size, size)

    def area(self):
        """Calculate the distance inside"""
        return self.width * self.height

    def perimeter(self):
        """The distance all the way around the outside"""
        return 2 * (self.width + self.height)\
            if self.width and self.height\
            else 0

    def __str__(self):
        """printable ``Rectangle``"""
        _str = ''
        if (not self.width or not self.height):
            return _str
        for i in range(self.height):
            _str += str(self.print_symbol) * self.width\
                    + ('', '\n')[i < self.height - 1]
        return _str

    def __repr__(self):
        """Return representation.
        of the rectangle to be able to recreate a new instance by using eval()
        """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Delete instance."""
        if Rectangle.number_of_instances:
            Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
