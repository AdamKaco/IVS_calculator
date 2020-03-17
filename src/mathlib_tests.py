## @file mathlib_tests.py
# @author Simon Kosina
# @date 9.3.2020
# @brief Tests for mathlib.py

import unittest
import mathlib

## @brief Tests for addition
class TestAddition(unittest.TestCase):

    def test_sum(self):
        # Test boundaries
        self.assertEqual(mathlib.sum(1,0), 1)
        self.assertEqual(mathlib.sum(-1,0), -1)
        self.assertEqual(mathlib.sum(0,1), 1)
        self.assertEqual(mathlib.sum(0,-1), -1)
        
        # Equals zero
        self.assertEqual(mathlib.sum(0,0), 0)
        self.assertEqual(mathlib.sum(-7,7), 0)
        self.assertEqual(mathlib.sum(7,-7), 0)

        # Pos and neg combinations for a > b
        self.assertEqual(mathlib.sum(7,3),10)
        self.assertEqual(mathlib.sum(7,-3),4)
        self.assertEqual(mathlib.sum(-7,3),-4)
        self.assertEqual(mathlib.sum(-7,-3),-10)
        
        # Pos and neg combinations for a < b
        self.assertEqual(mathlib.sum(3,7),10)
        self.assertEqual(mathlib.sum(-3,7),4)
        self.assertEqual(mathlib.sum(3,-7),-4)
        self.assertEqual(mathlib.sum(-3,-7),-10)

## @brief Tests for subtraction
class TestSubtraction(unittest.TestCase):

    def test_sub(self):
        # Test boundaries
        self.assertEqual(mathlib.sub(1,0), 1)
        self.assertEqual(mathlib.sub(-1,0), -1)
        self.assertEqual(mathlib.sub(0,1), -1)
        self.assertEqual(mathlib.sub(0,-1), 1)
                                   
        # Equals zero              
        self.assertEqual(mathlib.sub(0,0), 0)
        self.assertEqual(mathlib.sub(7,7), 0)
        self.assertEqual(mathlib.sub(-7,-7), 0)
                                   
        # Pos and neg combinations for a > b
        self.assertEqual(mathlib.sub(7,3),4)
        self.assertEqual(mathlib.sub(7,-3),10)
        self.assertEqual(mathlib.sub(-7,3),-10)
        self.assertEqual(mathlib.sub(-7,-3),-4)
                                   
        # Pos and neg combinations for a < b
        self.assertEqual(mathlib.sub(3,7),-4)
        self.assertEqual(mathlib.sub(-3,7),-10)
        self.assertEqual(mathlib.sub(3,-7),10)
        self.assertEqual(mathlib.sub(-3,-7),4)
   
## @brief Tests for multiplication
class TestMultiplication(unittest.TestCase):

    def test_mul(self):
        # Multiplication by 0
        self.assertEqual(mathlib.mul(1,0), 0)
        self.assertEqual(mathlib.mul(-1,0), 0)
        self.assertEqual(mathlib.mul(0,1), 0)
        self.assertEqual(mathlib.mul(0,-1), 0)
        self.assertEqual(mathlib.mul(0,0), 0)
        
        # Pos and neg combinations for a = b
        self.assertEqual(mathlib.mul(7,7), 49)
        self.assertEqual(mathlib.mul(-7,7), -49)
        self.assertEqual(mathlib.mul(7,-7), -49)
        self.assertEqual(mathlib.mul(-7,-7), 49)
                                   
        # Pos and neg combinations for a > b
        self.assertEqual(mathlib.mul(7,3),21)
        self.assertEqual(mathlib.mul(7,-3),-21)
        self.assertEqual(mathlib.mul(-7,3),-21)
        self.assertEqual(mathlib.mul(-7,-3),21)
                                   
        # Pos and neg combinations for a < b
        self.assertEqual(mathlib.mul(3,7),21)
        self.assertEqual(mathlib.mul(-3,7),-21)
        self.assertEqual(mathlib.mul(3,-7),-21)
        self.assertEqual(mathlib.mul(-3,-7),21)

## @brief Tests for division
class TestDivision(unittest.TestCase):
    
    def test_div(self):
        # Division by 0
        self.assertRaises(ZeroDivisionError, mathlib.div, 1, 0)
        self.assertRaises(ZeroDivisionError, mathlib.div, -1, 0)

        # Pos and neg combinations for a = b
        self.assertEqual(mathlib.div(7,7), 1)
        self.assertEqual(mathlib.div(-7,7), -1)
        self.assertEqual(mathlib.div(7,-7), -1)
        self.assertEqual(mathlib.div(-7,-7), 1)

        # Pos and neg combinations for a > b
        self.assertEqual(mathlib.div(10,2),5)
        self.assertEqual(mathlib.div(10,-2),-5)
        self.assertEqual(mathlib.div(-10,2),-5)
        self.assertEqual(mathlib.div(-10,-2),5)
                                   
        # Pos and neg combinations for a < b
        self.assertEqual(mathlib.div(2,10),0.2)
        self.assertEqual(mathlib.div(-2,10),-0.2)
        self.assertEqual(mathlib.div(2,-10),-0.2)
        self.assertEqual(mathlib.div(-2,-10),0.2)

        # Try some periodic results
        self.assertAlmostEqual(mathlib.div(1,3), 1/3)

## @brief Tests for computing factorial
class TestFactorial(unittest.TestCase):

    def test_fact(self):
        # n is not an integer
        self.assertRaises(TypeError, mathlib.fact, 2.5)
        self.assertRaises(TypeError, mathlib.fact, -3.121)
        
        # n < 0
        self.assertRaises(ValueError, mathlib.fact, -1)
        self.assertRaises(ValueError, mathlib.fact, -319)

        # n = 0
        self.assertEqual(mathlib.fact(0), 1)

        # n > 0
        self.assertEqual(mathlib.fact(1), 1)
        self.assertEqual(mathlib.fact(3), 6)
        self.assertEqual(mathlib.fact(10), 3628800)

## @brief Tests for exponentiation
class TestExponentiation(unittest.TestCase):

    def test_exp(self):
        # n is not an integer
        self.assertRaises(TypeError, mathlib.exp, 1, 2.5)

        # x = 0 and n < 0
        self.assertRaises(ValueError, mathlib.exp, 0, -1)
        self.assertRaises(ValueError, mathlib.exp, 0, -5)

        # x = 0
        self.assertEqual(mathlib.exp(0,0),1)
        self.assertEqual(mathlib.exp(0,1),0)
        self.assertEqual(mathlib.exp(0,7),0)
                        
        # x < 0 and n = 0
        self.assertEqual(mathlib.exp(-1,0),1)
        self.assertEqual(mathlib.exp(-10,0),1)
                        
        # x < 0 and n < 0
        self.assertEqual(mathlib.exp(-1,-1),-1)
        self.assertEqual(mathlib.exp(-1,-2),1)
        self.assertEqual(mathlib.exp(-1,-5),-1)
        self.assertEqual(mathlib.exp(-10,-1),-1/10)
        self.assertEqual(mathlib.exp(-2.5,-2),1/(2.5*2.5))
        self.assertEqual(mathlib.exp(-10,-5),-1/100000)           
        
        # x < 0 and n > 0
        self.assertEqual(mathlib.exp(-1,1),-1)
        self.assertEqual(mathlib.exp(-1,2),1)
        self.assertEqual(mathlib.exp(-1,5),-1)
        self.assertEqual(mathlib.exp(-10,1),-10)
        self.assertEqual(mathlib.exp(-2.5,2),2.5*2.5)
        self.assertEqual(mathlib.exp(-10,5),-100000)
                        
        # x > 0 and n = 0
        self.assertEqual(mathlib.exp(1,0), 1)
        self.assertEqual(mathlib.exp(10,0), 1)
                        
        # x > 0 and n < 0
        self.assertEqual(mathlib.exp(1,-1),1)
        self.assertEqual(mathlib.exp(1,-2),1)
        self.assertEqual(mathlib.exp(1,-5),1)
        self.assertEqual(mathlib.exp(10,-1),1/10)
        self.assertEqual(mathlib.exp(2.5,-2),1/(2.5*2.5))
        self.assertEqual(mathlib.exp(10,-5),1/100000)
                        
        # x > 0 and n > 0
        self.assertEqual(mathlib.exp(1,1),1)
        self.assertEqual(mathlib.exp(1,2),1)
        self.assertEqual(mathlib.exp(1,5),1)
        self.assertEqual(mathlib.exp(10,1),10)
        self.assertEqual(mathlib.exp(2.5,2),2.5*2.5)
        self.assertEqual(mathlib.exp(10,5),100000)

## @brief Tests for computing the n-th root
class TestRoot(unittest.TestCase):

    def test_root(self):
        # n = 0
        self.assertRaises(ZeroDivisionError, mathlib.root, 2, 0)
        
        # n not an integer
        self.assertRaises(TypeError, mathlib.root, 2, 1.5)
        self.assertRaises(TypeError, mathlib.root, 2, -7.7)

        # n > 0 and even
        self.assertRaises(ValueError, mathlib.root, -1, 2) # x must be > 0        
        # x > 0
        self.assertEqual(mathlib.root(4, 2), 2)
        self.assertEqual(mathlib.root(16, 4), 2)
        # x = 0
        self.assertEqual(mathlib.root(0, 2), 0)
        self.assertEqual(mathlib.root(0, 4), 0)

        # n > 0 and odd
        # x < 0
        self.assertEqual(mathlib.root(-3, 1), -3)
        self.assertEqual(mathlib.root(-27, 3), -3)
        # x > 0
        self.assertEqual(mathlib.root(3, 1), 3)
        self.assertEqual(mathlib.root(27, 3), 3)
        # x = 0
        self.assertEqual(mathlib.root(0, 1), 0)
        self.assertEqual(mathlib.root(0, 3), 0)

        # n < 0 and even
        self.assertRaises(ValueError, mathlib.root, -1, -2) # x must be > n        
        # x > 0
        self.assertEqual(mathlib.root(4, -2), 0.5)
        self.assertEqual(mathlib.root(16, -4), 0.5)
        # x = 0
        self.assertRaises(ValueError, mathlib.root, 0, -2)
        
        # n < 0 and odd
        # x < 0
        self.assertEqual(mathlib.root(-2, -1), -0.5)
        self.assertEqual(mathlib.root(-3125, -5), -0.2)
        # x > 0
        self.assertEqual(mathlib.root(2, -1), 0.5)
        self.assertEqual(mathlib.root(3125, -5), 0.2)
        # x = 0
        self.assertRaises(ValueError, mathlib.root, 0, -5)

## @brief Tests for computing combination numbers
class TestCombination(unittest.TestCase):

    def test_comb(self):
        # n or k is not an integer
        self.assertRaises(TypeError, mathlib.comb, 2.5, 1)
        self.assertRaises(TypeError, mathlib.comb, 5, 2.5)
        self.assertRaises(TypeError, mathlib.comb, 7.7, 5.5)

        # n or k is not non-negative
        self.assertRaises(ValueError, mathlib.comb, 2, -1)
        self.assertRaises(ValueError, mathlib.comb, -2, 1)
        self.assertRaises(ValueError, mathlib.comb, -1, -5)

        # k > n
        self.assertRaises(ValueError, mathlib.comb, 1, 2)
        self.assertRaises(ValueError, mathlib.comb, 0, 1)

        # k = 0
        self.assertEqual(mathlib.comb(2,0), 1)
        self.assertEqual(mathlib.comb(5,0), 1)
                                            
        # k = 1                              
        self.assertEqual(mathlib.comb(2,1), 2)
        self.assertEqual(mathlib.comb(5,1), 5)
                                             
        # k = n                              
        self.assertEqual(mathlib.comb(2,2), 1)
        self.assertEqual(mathlib.comb(5,5), 1)

        # some other values
        self.assertEqual(mathlib.comb(7,3), 35)
        self.assertEqual(mathlib.comb(13,2), 78)
        self.assertEqual(mathlib.comb(25,3), 2300)


if __name__ == "__main__":
    unittest.main()
