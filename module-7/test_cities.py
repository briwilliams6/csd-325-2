import unittest
from city_functions import location

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_city = location ('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()