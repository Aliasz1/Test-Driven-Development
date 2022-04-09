from operator import ge
import unittest
from stringProvider import get

class stringTester(unittest.TestCase):
    def test_string_check(self):
        self.assertEqual(get(), 'this is a test string')
        
if __name__ == '__main__':
    unittest.main()