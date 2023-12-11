#!/usr/bin/python3
"""Module defines Base class."""

from json import dumps, loads


class Base:
    """Create `id`.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)

    Attributes:
        __nb_objects(int): number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or not list_dictionaries:
            return dumps([])
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""

        return loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: list of dictionaries
        """

        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string
                    ([o.to_dictionary() for o in list_objs]
                     if isinstance(list_objs, list) else []))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Notes:
            the function creates new instance from `Rectangle` or `Square`
            and initializes positional args w/ 1

        Examples:
            >>> r = Rectangle(1, 1)
            >>> print(r)
            [Rectangle] (1) 0/0 - 1/1
            >>> s = Square(1, 1)
            >>> print(s)
            [Square] (1) 1/0 - 1
        """

        name = cls.__name__
        obj = getattr(__import__(name.lower()), name)(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances

        Notes:
            - The filename must be: <Class name>.json
            - If the file doesn’t exist, return an empty list
        """

        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                return [cls.create(**d)
                        for d in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes CSV file

        Notes:
            - The filename must be: <Class name>.csv
            - format:
                + Rectangle: <id>,<width>,<height>,<x>,<y>
                + Square: <id>,<size>,<x>,<y>
        """

        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as f:
            cls_attrs = ('id', 'width', 'height', 'x', 'y')\
                    if cls.__name__ == 'Rectangle'\
                    else ('id', 'size', 'x', 'y')

            f.write(''.join([','.join([str(o.to_dictionary()[k])
                                       for k in cls_attrs]) + '\n'
                             for o in list_objs]) if list_objs else '')

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV file"""

        cls_attrs = ('id', 'width', 'height', 'x', 'y')\
            if cls.__name__ == 'Rectangle' else ('id', 'size', 'x', 'y')
        try:
            with open(cls.__name__ + '.csv', 'r', encoding='utf-8') as f:
                return [cls.create(**{cls_attrs[i]: int(n)
                                      for i, n in enumerate(line.split(','))})
                        for line in f]
        except FileNotFoundError:
            return []
