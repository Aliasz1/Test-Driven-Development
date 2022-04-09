import unittest
from calculator import Calculator

class testProblem(unittest.TestCase):
    def test_calculation(self):
        calculator = Calculator(2)
        self.assertEqual(calculator.output, 2)
        
if __name__ == '__main__':
    unittest.main()