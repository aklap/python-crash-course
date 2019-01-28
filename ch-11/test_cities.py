import unittest
from city_functions import format


class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test address function concatenates args."""
        formatted_location = format('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')


    def test_city_country_population(self):
        """Test population arg is joined with string."""
        formatted_location = format('santiago', 'chile', '5000000')
        self.assertEqual(formatted_location, 'Santiago, Chile - 5000000')


unittest.main()
