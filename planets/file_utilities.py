import json
from planet import Planet

class FileUtilities:
    def load_planets(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Planet(**planet) for planet in data]
        