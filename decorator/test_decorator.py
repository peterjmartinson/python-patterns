import unittest
from decorator import *

class Test_Value(unittest.TestCase):
    
    def setUp(self):
        self.value = Value()

    def test_setValue_exists(self):
        self.assertTrue(hasattr(self.value, 'setValue'))

    def test_getValue_exists(self):
        self.assertTrue(hasattr(self.value, 'getValue'))

    def test_setValue_works(self):
        self.value.setValue(10)
        result = self.value.value
        self.assertEqual(result, 10)

    def test_getValue_works(self):
        self.value.value = 25
        result = self.value.getValue()
        self.assertEqual(result, 25)

class Test_Decorator(unittest.TestCase):
    
    def setUp(self):
        self.value = Value()
        self.decorator = DecorateValue()

    def test_addFourToValue_exists(self):
        self.assertTrue(hasattr(self.decorator, 'addFourToValue'))

    def test_addFourToValue_works(self):
        self.value.value = 25
        result = self.decorator.addFourToValue(self.value.getValue())
        self.assertEqual(result, 29)
