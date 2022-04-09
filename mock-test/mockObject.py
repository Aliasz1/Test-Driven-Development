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
        m.get_number.return_value = 2
        self.assertEqual(m.get_number, 2)
        
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
        m.get_number.return_value = 2
        
        m.get_number.side_effect = [3, 4, 5]
        self.assertEqual(m.get_number(), 3)
        self.assertEqual(m.get_number(), 4)
        self.assertEqual(m.get_number(), 5)
        
    def test_verify(self):
        m = mock.Mock()
        m.called.return_value = 2
        m.called()
        m.called.assert_called()
        
    def test_verify_multiple(self):
        m = mock.Mock()
        m.called.return_value = 2
        m.called()
        m.called.assert_called()
        m.called.assert_called()
        m.called.assert_called()
        self.assertEqual(m.called.count, 3)
        
    def test_verify_reset(self):
        m = mock.Mock()
        m.called.return_value = 2
        m.called()
        m.called.assert_called()
        m.called.assert_called()
        m.called.assert_called()
        m.called.reset_mock()
        self.assertEqual(m.called.count, 0)
        
if __name__ == '__main__':
    unittest.main()