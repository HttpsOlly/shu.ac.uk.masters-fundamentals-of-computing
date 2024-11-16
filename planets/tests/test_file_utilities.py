import unittest
from unittest.mock import patch, mock_open
from planet import Planet
from file_utilities import FileUtilities

class TestLoadPlanets(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='[{"name": "Planet", "mass": 1.0e+23, "distance": 12345678, "number_of_moons": 1, "moons": ["Moon"]}]')
    def test_load_planets(self, mock_file):
        planets = FileUtilities.load_planets('planets.json')
        self.assertEqual(len(planets), 1)
        self.assertIsInstance(planets[0], Planet)
        self.assertEqual(planets[0].name, "Planet")
        self.assertEqual(planets[0].mass, 1.0e+23)
        self.assertEqual(planets[0].distance, 12345678)
        self.assertEqual(planets[0].moons, ["Moon"])

if __name__ == '__main__':
    unittest.main()