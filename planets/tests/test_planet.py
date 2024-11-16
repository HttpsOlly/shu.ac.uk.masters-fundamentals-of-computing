import unittest
from unittest.mock import patch, mock_open
from planet import Planet

class TestPlanetZeroMoons(unittest.TestCase):
    def setUp(self):
        self.planet = Planet("Planet Name", 1e+23, 123456789, 0, [])

    def test_planet_attributes(self):
        self.assertEqual(self.planet.name, "Planet Name")
        self.assertEqual(self.planet.mass, 1e+23)
        self.assertEqual(self.planet.distance, 123456789)
        self.assertEqual(self.planet.number_of_moons, 0)
        self.assertEqual(self.planet.moons, [])

    def test_to_string(self):
        expected_output = (
            "Name: Planet Name\n"
            "Mass: 1e+23 kg\n"
            "Distance from the Sun: 123456789 km\n"
            "Number of Moons: 0\n"
        )
        with patch('builtins.print') as mocked_print:
            str = self.planet.to_string()
            self.assertEqual(str, expected_output)

class TestPlanetOneMoon(unittest.TestCase):
    def setUp(self):
        self.planet = Planet("Planet Name", 1e+23, 123456789, 1, ["Moon"])

    def test_planet_attributes(self):
        self.assertEqual(self.planet.name, "Planet Name")
        self.assertEqual(self.planet.mass, 1e+23)
        self.assertEqual(self.planet.distance, 123456789)
        self.assertEqual(self.planet.number_of_moons, 1)
        self.assertEqual(self.planet.moons, ["Moon"])

    def test_to_string(self):
        expected_output = (
            "Name: Planet Name\n"
            "Mass: 1e+23 kg\n"
            "Distance from the Sun: 123456789 km\n"
            "Number of Moons: 1\n"
            "Here the moons I know about: Moon\n"
        )
        with patch('builtins.print') as mocked_print:
            str = self.planet.to_string()
            self.assertEqual(str, expected_output)

if __name__ == '__main__':
    unittest.main()