import unittest

import math
import re
from Tkinter import *
import tkMessageBox as box
import calculator_test as c




class CalcTest(unittest.TestCase):
    
   
    #expected error grants no pop-up windows
    c.errFlag = False


    def test_factorial_1(self):
        self.assertEqual(c.factorial(3),6)

    def test_factorial_2(self):
        self.assertEqual(c.factorial(0),1)

    def backspace(self):
        
        c.stack.clear()

        c.string.set("4")
        c.delete()
        self.assertEqual(c.string.get(), "")

    def test_multiply_zero(self):

        c.stack.clear()

        c.string.set("4 * 0")
        c.getResult()
        self.assertEqual(c.string.get(), "0.0")
        

    
    def test_multiply(self): 

        c.stack.clear()

        c.string.set("4 * 6")        
        c.getResult()
        self.assertEqual(c.string.get(), "24.0")
    
    def test_divide_zero(self):       
        
        c.stack.clear()

        c.string.set("6 / 0")        
        c.getResult()
        self.assertEqual(c.string.get(), "6 / 0")

    def test_divide(self):       
        
        c.stack.clear()
        
        c.string.set("6 / 2.5")        
        c.getResult()
        self.assertEqual(c.string.get(), "2.4")

    
    def test_power(self):

        c.stack.clear()

        c.string.set("6 ^ 2")
        c.getResult()
        self.assertEqual(c.string.get(), "36.0")
    
    def test_brackets(self):

        c.stack.clear()

        c.string.set("( 4 +  4 ) * 2" )
        c.getResult()
        self.assertEqual(c.string.get(), "16.0")

    def test_minus(self):

        c.stack.clear()

        c.string.set("6 - 4")
        c.getResult()
        self.assertEqual(c.string.get(), "2.0")

    def test_minus_negative(self):

        c.stack.clear()

        c.string.set("6 - 74")
        c.getResult()
        self.assertEqual(c.string.get(), "-68.0")

    def test_singleNumberPrint(self):

       c.stack.clear()

       c.string.set("6")
       c.getResult()
       self.assertEqual(c.string.get(), "6.0")


    def test_addition(self):

       c.stack.clear()

       c.string.set("4 + 8")
       c.getResult()
       self.assertEqual(c.string.get(), "12.0")

    def test_addition_neg(self):

       c.stack.clear()

       c.string.set("-2 + 6")
       c.getResult()
       self.assertEqual(c.string.get(), "4.0")

    def test_negation(self):

       c.stack.clear()

       c.string.set("6")
       c.negation()
       self.assertEqual(c.string.get(), "-6")

    def test_negation_2(self):

       c.stack.clear()

       c.string.set("-6")
       c.negation()
       self.assertEqual(c.string.get(), "6")

    def test_clear(self):

       c.stack.clear()

       c.string.set("7")
       c.clear()
       self.assertEqual(c.string.get(), "0")

    def test_sin(self):

       c.stack.clear()

       c.string.set("sin 0")
       c.getResult()
       self.assertEqual(c.string.get(), "0.0")

    def test_cos(self):

       c.stack.clear()

       c.string.set("cos 0")
       c.getResult()
       self.assertEqual(c.string.get(), "1.0")

    def test_log(self):

       c.stack.clear()

       c.string.set("log 10")
       c.getResult()
       self.assertEqual(c.string.get(), "1.0")


    def test_ln(self):

        c.stack.clear()

        c.string.set("ln 1")
        c.getResult()
        self.assertEqual(c.string.get(), "0.0")


    def test_tan(self):

        c.stack.clear()

        c.string.set("tan 1")
        c.getResult()
        self.assertEqual(c.string.get(), "1.55740772465")


    def test_cotan(self):

        c.stack.clear()

        c.string.set("0")
        c.getResult()
        self.assertEqual(c.string.get(), "0.0")

    def test_expression(self):

        c.stack.clear()

        c.string.set("( 2 * 4 - ( 7 / 7 ) + 2 ) * 3 + 4")
        c.getResult()
        self.assertEqual(c.string.get(), "31.0")


   
      

if __name__ == '__main__':
    unittest.main()