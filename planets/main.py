from file_utilities import FileUtilities

def main():
    planets = FileUtilities.load_planets('planets.json')
    for planet in planets:
        print(planet.to_string())

if __name__ == "__main__":
    main()
