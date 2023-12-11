#!/usr/bin/python3
"""Unittest for `Base` class
"""

import unittest
import pep8
from models.base import Base


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

    def test_serialize_json(self):
        """ """
        pass

    def test_deserialize_json(self):
        """ """
        pass
