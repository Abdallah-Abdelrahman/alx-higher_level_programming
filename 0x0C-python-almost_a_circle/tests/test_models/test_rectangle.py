#!/usr/bin/python3
"""Unittest for `Rectangle` class
"""

import io
import unittest
from unittest.mock import patch

from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_cls_doc(self):
        """Test class doc """
        self.assertFalse(len(Rectangle.__doc__) == 0)

    def test_init(self):
        """Test __init__"""
        r0 = Rectangle(10, 2, 0, 0, -1)
        self.assertEqual(r0.id, -1)

    def test_init1(self):
        """Test"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 9)

    def test_init2(self):
        """Test"""
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 10)

    def test_init3(self):
        """Test"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_setter_fail_w(self):
        """Test width/height"""
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 1, 0, 0, 0)

    def test_setter_fail_w1(self):
        """Test width"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('10', 2)

    def test_setter_fail_h(self):
        """Test width/height"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, 0, 1, 1, 1)

    def test_setter_x(self):
        """Test x/y"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, '3', 4, 5)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(1, 2, -1, 4, 5)

    def test_setter_y(self):
        """Test x/y"""
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(10, 2, 3, -1)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(10, 2, 3, '4', 1)

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

    def test_display_xy(self):
        """Test display"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1 = Rectangle(2, 2, 1, 0, 0)
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), ' ##\n ##\n')

    def test_display_fail(self):
        """Test fialing scenarios"""

        r = Rectangle(1, 1, 0, 0, 0)
        self.assertRaises(TypeError, r.display, '#')

    def test_str(self):
        """Test __str__"""

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r = Rectangle(1, 1, 0, 0, 0)
            print(r)
            self.assertEqual(mock_stdout.getvalue().strip(),
                             '[Rectangle] (0) 0/0 - 1/1')

    def test_update(self):
        """Test update"""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        with self.assertRaises(ValueError):
            r1.update(width=0)

    def test_to_dictionary(self):
        """Test to_dictionary"""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            _str = "{'x': 1, 'y': 9, 'id': 18, 'height': 2, 'width': 10}"

            print(r1_dictionary)
            self.assertEqual(mock_stdout.getvalue().strip(), _str)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(type(r1_dictionary))
            self.assertEqual(mock_stdout.getvalue().strip(), "<class 'dict'>")

    def test_create(self):
        """Test create"""
        r1 = Rectangle(3, 3, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            print(r1)
            self.assertEqual(m_stdout.getvalue(),
                             '[Rectangle] (7) 1/1 - 3/3\n')
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            print(r2)
            self.assertEqual(m_stdout.getvalue(),
                             '[Rectangle] (7) 1/1 - 3/3\n')
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            self.assertFalse(r1 is r2)
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            self.assertFalse(r1 == r2)
        with self.assertRaises(TypeError):
            Rectangle.create(None)

    def test_load_from_file(self):
        """Test `load_from_file`"""

        r1 = Rectangle(10, 7, 2, 8, 0)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            for rect in list_rectangles_output:
                print("{}".format(rect))
                self.assertEqual(m_stdout.getvalue(),
                                 '[Rectangle] (0) 2/8 - 10/7\n')
        Rectangle.save_to_file(None)
        output2 = Rectangle.load_from_file()
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            for rect in output2:
                print("{}".format(rect))
                self.assertEqual(m_stdout.getvalue(), [])
        s = Square(1, 1, 1, 1)
        Square.save_to_file([s])
        output2 = Square.load_from_file()
        with patch('sys.stdout', new_callable=io.StringIO) as m_stdout:
            print("{}".format(output2[0]))
            self.assertEqual(m_stdout.getvalue(),
                             '[Square] (1) 1/1 - 1\n')
