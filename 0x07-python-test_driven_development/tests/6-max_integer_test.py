#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer function."""

    def test_max_in_middle(self):
        """Test max in middle"""

        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_emptylist(self):
        """Test empty list"""

        self.assertEqual(max_integer(), None)

    def test_one_item_list(self):
        """Test list w/ one item."""

        self.assertEqual(max_integer([1]), 1)

    def test_negative_items_list(self):
        """Test list w/ negative item."""

        self.assertEqual(max_integer([-1, 0]), 0)

    def test_diff_list(self):
        """Test list w/ different items data type."""

        self.assertRaises(TypeError, max_integer, ['1', 2])


    def test_str_list(self):
        """Test list w/ str items."""

        self.assertEqual(max_integer(['1', '0']), '1')
