class Planet(object):
    def __init__(self, name, mass, distance, number_of_moons, moons):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.number_of_moons = number_of_moons
        self.moons = moons

    def to_string(self):
        str = f"Name: {self.name}\n"
        str += f"Mass: {float(self.mass)} kg\n"
        str += f"Distance from the Sun: {self.distance} km\n"
        str += f"Number of Moons: {self.number_of_moons}\n"
        if (self.moons):
            str +=f"Here the moons I know about: {', '.join(self.moons)}\n"
        return str