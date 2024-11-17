from file_utilities import FileUtilities
from interface_menu import InterfaceMenu

def main():
    planets = FileUtilities.load_planets('planets.json')
    InterfaceMenu.display_main_menu(planets)

if __name__ == "__main__":
    main()
