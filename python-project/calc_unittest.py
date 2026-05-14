import unittest
from calculator import add, sub

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(1,1),2)   # fixed

    def test_sub(self):
        self.assertEqual(sub(-1,2),-3)








