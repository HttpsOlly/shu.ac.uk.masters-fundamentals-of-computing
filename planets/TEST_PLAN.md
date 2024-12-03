# Test Plan

| #   | Scenario   | Expected Result | Latest Result | Automated | 
|:--- | ---------- | --------------- |:-------------:|:---------:|
| 1 | Assert that a Planet class can be instantiated | | |
| 1.1 | With zero moons | object of class Planet | Pass | Yes |
| 1.2 | With one or more moons | object of class Planet | Pass | Yes |
| 2 | Assert that planets can be loaded from a file | | |
| 2.1 | Happy path where planets have any number of moons | list of Planet objects | Pass | Yes |
| 2.2 | Unhappy path using defensive programming loading a malformed file | Exception handled, user informed | Pass | Yes |
| 3 | Request a list of planets | list of planets provided | Pass | No |
| 4 | Request information about a specific planet | the name, mass, distance from the sun and a list of the planet's moons (if any) is provided | Pass | No |
| 5 | Request the mass of a specific planet | the planet's mass is provided | Pass | No |
| 6 |Request number of moons of a specific planet | | |
| 6.1 | …with zero moons | no moons are provided | Pass | No |
| 6.2 | …with one moon | the moon is identified | Pass | No |
| 6.3 | …with more than one moon and fewer than 10 moons | all moons are listed | Pass | No |
| 6.4 | …with over 10 moons | only the ten largest moons are listed | Pass | No |