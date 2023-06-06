#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test when the list is not empty
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)

        # Test when the list is empty
        self.assertIsNone(max_integer([]))

        # Test with duplicate maximum values
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

if __name__ == '__main__':
    unittest.main()

