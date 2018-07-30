import unittest
from decorator import *

class Test_Value(unittest.TestCase):
    
    def setUp(self):
        self.value = Value()

    def test_value_exists_after_initializer(self):
        pass

    def test_setValue_exists(self):
        self.assertTrue(hasattr(self.value, 'setValue'))



    def test_getValue_exists(self):
        self.assertTrue(hasattr(self.value, 'getValue'))

