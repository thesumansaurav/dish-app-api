"""Sample Test"""

from django.test import SimpleTestCase
from app import calculator

class TestCalculator(SimpleTestCase):
    """Test the calculator functions"""

    def test_add_numbers(self):
        """Test for add function in the calculator.py"""
        result= calculator.add(15,61)
        self.assertEqual(result, 76)

    def test_sub_numbers(self):
        result= calculator.substract(15,25)
        self.assertEqual(result, 10)