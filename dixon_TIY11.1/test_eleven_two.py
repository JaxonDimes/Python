import unittest
from eleven_two import placement

class CountryTestCase(unittest.TestCase):
    def country_test(self):
        """Does Santiago, Chile work?"""
        cont = placement('santiago', 'chile', 12)
        self.assertEqual(cont, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()

