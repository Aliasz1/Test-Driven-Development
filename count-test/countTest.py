import unittest
from countlist import CountList

class countTest(unittest.TestCase):
    def compareList(self):
        countlist = CountList()
        count = countlist.getAll()
        self.assertCountEqual(countlist, [])
        
if __name__ == '__main__':
    unittest.main()