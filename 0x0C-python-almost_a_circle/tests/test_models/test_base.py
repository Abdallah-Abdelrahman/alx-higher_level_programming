#!/usr/bin/python3
"""Unittest for `Base` class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class"""
    def test_with_id(self):
        """Test with id passed"""
        base = Base(2)
        self.assertEqual(base.id, 2)

    def test_wout_id(self):
        """Test w/out arg"""
        base = Base()
        self.assertEqual(base.id, 1)
