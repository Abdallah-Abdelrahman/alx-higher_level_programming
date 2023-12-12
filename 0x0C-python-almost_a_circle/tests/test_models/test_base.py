#!/usr/bin/python3
"""Unittest for `Base` class
"""

import io
import unittest
from unittest.mock import patch
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test Base class"""

    def test_pep8_base(self):
        """Test that the base module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_cls_doc(self):
        """Test class doc """

        self.assertFalse(len(Base.__doc__) == 0)

    def test_init(self):
        """Test __init__"""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_to_json(self):
        """Serialization test"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            _str = "{'x': 2, 'y': 8, 'id': 5, 'height': 7, 'width': 10}"
            print(dictionary)
            self.assertEqual(mock_stdout.getvalue().strip(), _str)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(type(dictionary))
            self.assertEqual(mock_stdout.getvalue(), "<class 'dict'>\n")
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            _str = '[{"x": 2, "y": 8, "id": 5, "height": 7, "width": 10}]'
            print(json_dictionary)
            self.assertEqual(mock_stdout.getvalue().strip(), _str)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(type(json_dictionary))
            self.assertEqual(mock_stdout.getvalue(), "<class 'str'>\n")
