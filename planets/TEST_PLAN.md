# Test Plan
1. Assert that a Planet class can be instantiated
    1. With zero moons
    1. With one or more moons
1. Assert that planets can be loaded from a file 
    1. Happy path where planets have any number of moons
    1. Unhappy path using defensive programming loading a malformed file
1. When a list of planets is requested, a list of planets is provided
    1. When asking for information about a specific planet, then the name, mass, distance from the sun and a list of the planet's moons (if any) is provided
    1. When asking about the mass of a specific planet, the planet's mass is provided
    1. When asking about how many moons a specific planet has, the number of moons a planet has is provided, and known moons are listed
        1. Should a planet have zero moons, this is communicated
        1. Should a planet have one moon, the moon will be named
        1. Should a planet have more than one moon and fewer than 10 moons, all moons are listed
        1. Should a planet have over 10 moons, only the ten largest moons are listed
