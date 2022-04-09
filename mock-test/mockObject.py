import unittest
from unittest import mock

class mockObjectTest(unittest.TestCase):
    def test(self):
        mock_object = mock.Mock()
        assert isinstance(mock_object.field, mock.Mock)
        assert isinstance(mock_object.field2, mock.Mock)
        assert isinstance(mock_object(), mock.Mock)
        assert mock_object.field is not mock_object.field2 is not mock_object()
        
    def test_fields(self):
        m = mock.Mock()
        m.string = 'this string'
        self.assertEqual(m.string, 'this string')
        
        m.configure_mock(tdd='tester')
        self.assertEqual(m.tdd, 'tester')
        
    def test_functions(self):
        m = mock.Mock()
        m.get_number.return_value = 1
        self.assertEqual(m.get_number, 1)
        
    def test_exceptions(self):
        m = mock.Mock()
        m.throwException.side_effect = RuntimeError('Error')
        
        try:
            m.throwException()
        except RuntimeError:
            assert True
        else:
            assert False
         
    def test_multi_return(self):
        m = mock.Mock()
        m.get_number.return_value = 1
        
        m.get_number.side_effect = [2, 3, 4]
        self.assertEqual(m.get_number(), 2)
        self.assertEqual(m.get_number(), 3)
        self.assertEqual(m.get_number(), 4)
        
if __name__ == '__main__':
    unittest.main()