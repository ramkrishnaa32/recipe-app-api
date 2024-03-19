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


