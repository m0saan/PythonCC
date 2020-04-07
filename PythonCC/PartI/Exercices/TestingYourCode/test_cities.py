import unittest
from City_country import city_country


class CityCountryTest(unittest.TestCase):
    """ Test for 'citycountry.py'. """

    def test_city_country(self):
        formated_city_country = city_country("Madrid", "Spain")
        self.assertEqual(formated_city_country, "Madrid, Spain")

    def test_city_country_population(self):
        formated_city_country = city_country("tokyo", "japan", 10000000)
        self.assertEqual(
            formated_city_country,
            "Tokyo, Japan - Population 10000000"
        )


unittest.main()
