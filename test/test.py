import unittest
from utils.gen import validate_date_in

class TestRegularExpression(unittest.TestCase):
    def test_date_valid(self):
        date="2022-12-22"
        response = validate_date_in(date)
        self.assertTrue(response)
        
    def test_date_not_valid(self):
        date="12-12-22"
        response = validate_date_in(date)
        self.assertFalse(response)  
        
    def test_date_not_valid_i(self):
        date="12-12-2012"
        response = validate_date_in(date)
        self.assertFalse(response)  

if __name__ == 'main':
    unittest.main()
