import unittest
from addition import add_numbers

class TestAddition(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)  # Test with integers
        self.assertEqual(add_numbers(-1, 1), 0)  # Test with negative numbers
        self.assertEqual(add_numbers(0.5, 0.5), 1.0)  # Test with floats

if __name__ == '__main__':
    unittest.main()
