# test the addition function is correct

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers_module(self):
        """Test adding number together"""
        res = calc.add(2, 3)

        self.assertEqual(res, 5)
