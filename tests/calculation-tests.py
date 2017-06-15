import sys
sys.path.append('../')
from src.entro import entropy, info_gain
import unittest

class test_calculations(unittest.TestCase):
    def test_entropy(self):
        # Test a simple case with 2 class supports of 2 and 3.
        self.assertEqual(round(entropy([2, 3]), 5), 0.97095)
        # Test a case where there is only one class. 
        self.assertEqual(entropy([4]), 0)
        # Test that ValueError exception is raised when a support = 0.
        with self.assertRaises(ValueError):
            entropy([1, 3, 0])
        # Test that ValueError exception is raised when a support < 0.
        with self.assertRaises(ValueError):
            entropy([1, 3, -5])

    def test_info_gain(self):
        # Test a simple split with two resulting children.
        gain = info_gain([[3, 1], [1, 5]], [4, 6])
        self.assertEqual(round(gain, 5), 0.25643)
        # Test that ValueError exception is raised when a split support = 0.
        with self.assertRaises(ValueError):
            info_gain([[1, 3, 0], [2, 5, 1]], [3, 2, 9])
        # Test that ValueError exception is raised when a split support < 0.
        with self.assertRaises(ValueError):
            info_gain([[1, 3, -5], [2, 5, 1]], [3, 2, 9])
        # Test that ValueError exception is raised when a parent support =  0.
        with self.assertRaises(ValueError):
            info_gain([[1, 3, 8], [2, 5, 1]], [3, 0, 9])
        # Test that ValueError exception is raised when a parent support < 0.
        with self.assertRaises(ValueError):
            info_gain([[1, 3, 5], [2, 5, 1]], [3, -6, 9])

    def test_split_info(self):
        # Test a simple split with two resulting children.
        info = split_info([[3, 1], [1, 5]], [4, 6])
        self.assertEqual(round(info, 5), 0.97095)

if __name__ == '__main__':
    unittest.main(exit=False)
