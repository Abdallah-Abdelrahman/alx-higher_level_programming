#!/usr/bin/python3
"""Unittest for `Square` class
"""

import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_cls_doc(self):
        """Test class doc """
        self.assertFalse(len(Square.__doc__) == 0)

    def test_init(self):
        """Test __init__"""
        pass
