#!/usr/bin/python3

"""Modulue define Student class"""


class Student:
    """Define one isntance method"""

    def __init__(self, first_name, last_name, age) -> None:
        """Initialize the isntance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        d = self.__dict__
        if isinstance(attrs, list) and\
                all([isinstance(a, str) for a in attrs]):
            return {a: d[a] for a in attrs if a in d}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
