import sys
sys.path.append('../')
from src.entro import calculate_entropy
import unittest

class test_calculations(unittest.TestCase):
    def test_calculates_entropy(self):
        # Test a simple case with 2 class supports of 2 and 3.
        self.assertEqual(round(calculate_entropy([2, 3]), 5), 0.97095)
        # Test a case where there is only one class. 
        self.assertEqual(calculate_entropy([4]), 0)
        # Test that a ValueError exception is raised when a support is = 0.
        self.assertRaises(ValueError, calculate_entropy([1, 3, 0]), 1234)
        # Test that a ValueError exception is raised when a support is < 0.
        self.assertRaises(ValueError, calculate_entropy([1, 3, -5]), 1234)

if __name__ == '__main__':
    unittest.main(exit=False)
