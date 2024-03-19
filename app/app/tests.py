"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc


class CalsTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        """Validating the result"""
        self.assertEqual(res, 11)


    def test_substract_numbers(self):
        """Test substract numbers together"""
        res = calc.substract(15, 5)

        """Validating the result"""
        self.assertEqual(res, 10)
     