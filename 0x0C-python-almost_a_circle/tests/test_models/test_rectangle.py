#!/usr/bin/python3
"""Unittest for `Rectangle` class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_cls_doc(self):
        """Test class doc """
        self.assertFalse(len(Rectangle.__doc__) == 0)

    def test_init(self):
        """Test __init__"""
        r0 = Rectangle(10, 2, 0, 0, -1)
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r0.id, -1)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 6)
        self.assertEqual(r3.id, 12)
