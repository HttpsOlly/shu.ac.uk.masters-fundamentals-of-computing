class Planet(object):
    def __init__(self, name, mass, distance, number_of_moons, moons):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(mass, (int, float)):
            raise TypeError("mass must be a number")
        if not isinstance(distance, (int, float)):
            raise TypeError("distance must be a number")
        if not isinstance(moons, list):
            raise TypeError("moons must be a list")
        if not all(isinstance(moon, str) for moon in moons):
            raise TypeError("all moons must be strings")

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
    
    def describe_mass(self):
        return f"The mass of {self.name} is {self.mass} kg\n"
    
    def describe_moons(self):
        if (self.number_of_moons == 1):
            str = f"{self.name} has 1 moon, it is named {self.moons[0]}"
        else:
            str = f"{self.name} has {self.number_of_moons} moons. "
            if (self.moons):
                str += f"Here the moons I know about: {', '.join(self.moons)}"
        return str + "\n"