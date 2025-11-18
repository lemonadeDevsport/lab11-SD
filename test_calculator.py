#https://github.com/lemonadeDevsport/lab11-SD
#Sofia De Los Santos

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):# 3 assertions
        self.assertEqual(add(3,4),7)
        self.assertEqual(add(-5,3),-2)
        self.assertEqual(add(0,0),0)
        self.assertNotEqual(add(4,7),12)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 4), -1)
        self.assertEqual(subtract(5, 12), -7)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertNotEqual(subtract(4, 7), 3)

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, -4), -12)
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(-1, -1), 1)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 6), 3.0)
        self.assertEqual(div(-5, 10), -2.0)
        self.assertAlmostEqual(div(3, 10), 3.3333333333333335)


    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10,100),2.0)
        self.assertAlmostEqual(logarithm(math.e,math.e**3),3.0)
        self.assertAlmostEqual(logarithm(2,8),3.0)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0,7)
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
       with self.assertRaises(ValueError):
           logarithm(3,0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(1,1), math.sqrt(2))
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(64),8.0)
        self.assertAlmostEqual(square_root(2), 1.41421356237)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
