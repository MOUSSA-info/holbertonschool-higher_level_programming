#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()

