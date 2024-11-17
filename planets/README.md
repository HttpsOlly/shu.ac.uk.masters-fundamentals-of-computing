# Planets 

Create a program that displays information about planets in our solar system. For each planet
your program should hold its:
- Name.
- Mass.
- Distance from the Sun.
- A list of the planet’s moons (be sensible, don’t include all of the moons for the large planets).

All data should be held using appropriate data types. Use Wikipedia to help with values.

A user should be able to query your data by asking questions such as:
- Tell me everything about Saturn?
- How massive is Neptune?
- Is Pluto in the list of planets?
- How many moons does Earth have?

You must write a test plan that covers key parts of your solution. You should include this as a separate file within your solution.

You should bring all your programming knowledge to bear on this task.
- You must use classes throughout your program.
- You should include code to properly validate inputs from the user.
- The raw data may be held in a file.
- You may build a simple menu system.
- You might create a GUI using Tkinter.
- You may want to use a unit testing framework to implement some, or all, of your test plan.

Notes:
- You must the Python Programming language.
- You must store your code in your repository on GitHub.
- Do not make a Web-based solution.
- Do not use a relational database.

# Test Plan
1. Assert that a Planet class can be instantiated
    1. With zero moons
    1. With one or more moons
1. Assert that planets can be loaded from a file 
    1. Happy path where planets have any number of moons
    1. Unhappy path using defensive programming loading a malformed file

# To test
```
python3 -m unittest discover -s tests
```