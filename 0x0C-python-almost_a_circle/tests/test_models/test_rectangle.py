#!/usr/bin/python3
"""Unittest for `Rectangle` class
"""

import io
import unittest
from unittest.mock import patch
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

    def test_setter_wh(self):
        """Test width/height"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r = Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(10, 2)
            r.width = -10

    def test_setter_xy(self):
        """Test x/y"""
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(10, 2, 3, -1)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(10, 2)
            r.x = {}

    def test_area(self):
        """Test area"""
        r1 = Rectangle(3, 2, 0, 0, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10, 0, 0, 5)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_area_fail(self):
        """Test failing cases"""

        r = Rectangle(3, 2, 0, 0, 2)
        self.assertRaises(TypeError, r.area, 1)

    def test_display(self):
        """Test display"""

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r = Rectangle(1, 1, 0, 0, 0)
            r.display()
            self.assertEqual(mock_stdout.getvalue().strip(), '#')

    def test_display_fail(self):
        """Test fialing scenarios"""

        r = Rectangle(1, 1, 0, 0, 0)
        self.assertRaises(TypeError, r.display, '#')
