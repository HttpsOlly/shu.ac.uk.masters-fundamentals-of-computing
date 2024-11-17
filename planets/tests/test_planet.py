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
        
        str = self.planet.to_string()
        self.assertEqual(str, expected_output)

    def test_describe_mass(self):
        str = self.planet.describe_mass()
        self.assertEqual(str, "The mass of Planet Name is 1e+23 kg\n")

    def test_describe_moons(self):
        str = self.planet.describe_moons()
        self.assertEqual(str, "Planet Name has 0 moons. \n")

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
    
        str = self.planet.to_string()
        self.assertEqual(str, expected_output)

    def test_describe_moons(self):
        str = self.planet.describe_moons()
        self.assertEqual(str, "Planet Name has 1 moon, it is named Moon\n")

class TestPlanetMultipleMoons(unittest.TestCase):
    def setUp(self):
        self.planet = Planet("Planet Name", 1e+23, 123456789, 2, ["Moon 1", "Moon 2"])

    def test_describe_moons(self):
        str = self.planet.describe_moons()
        self.assertEqual(str, "Planet Name has 2 moons. Here the moons I know about: Moon 1, Moon 2\n")

if __name__ == '__main__':
    unittest.main()