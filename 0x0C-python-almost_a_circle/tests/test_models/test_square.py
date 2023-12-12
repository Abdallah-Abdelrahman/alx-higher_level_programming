#!/usr/bin/python3
"""Unittest for `Square` class
"""

import io
import unittest
from unittest.mock import patch
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_cls_doc(self):
        """Test class doc """
        self.assertFalse(len(Square.__doc__) == 0)

    def test_init(self):
        """Test __init__"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_disply(self):
        """Test display"""

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1 = Square(3)
            s1.display()
            self.assertEqual(mock_stdout.getvalue(),
                             '###\n###\n###\n')

    def test_update(self):
        """Test update"""

        s1 = Square(5)

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.update(10)
            print(s1)
            self.assertEqual(mock_stdout.getvalue(),
                             '[Square] (10) 0/0 - 5\n')
