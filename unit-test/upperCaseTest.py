import unittest

class upperCaseTest(unittest.TestCase):
    def test_upper(self):
        string = 'test string'
        
        result = string.upper()
        
        self.assertEqual(result,'TEST STRING')

if __name__ == '__main__':
    unittest.main()