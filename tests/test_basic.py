import unittest
from src.calc import calculate_price

class TestBasic(unittest.TestCase):
    
    def test_calculate_price(self):
        result = calculate_price(100, 10)
        self.assertEqual(result, 90)
    
    def test_negative_price(self):
        pass
    
    # def test_user_creation(self):
    #     pass

if __name__ == '__main__':
    unittest.main()