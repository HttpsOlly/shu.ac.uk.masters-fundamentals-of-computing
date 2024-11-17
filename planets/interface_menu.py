class InterfaceMenu:

    @staticmethod
    def display_main_menu(planets):
        while True:
            print("Menu:")
            print("1. List the known planets in the Solar System")
            print("2. Tell me everything about...")
            print("3. What is the mass of...")
            print("4. How many moons does...")
            print("X. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                planet_names = [planet.name for planet in planets]
                str = f"Here are the {len(planets)} known planets in the Solar System: "
                print(str + ", ".join(planet_names) + "\n")
            elif choice == '2':
                InterfaceMenu.display_sub_menu(planets, "info")
            elif choice == '3':
                InterfaceMenu.display_sub_menu(planets, "mass")
            elif choice == '4':
                InterfaceMenu.display_sub_menu(planets, "moons")
            elif choice.upper() == 'X':
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def display_sub_menu(planets, action):
        print("Choose a planet:")
        for i, planet in enumerate(planets, start=1):
            print(f"{i}. {planet.name}")
        planet = int(input("Enter your choice: ")) - 1

        if 0 <= planet < len(planets):
            if action == "info":
                print(planets[planet].to_string())
            elif action == "mass":
                print(planets[planet].describe_mass())
            elif action == "moons":
                print(planets[planet].describe_moons())
            else:
                print("Invalid choice. Please try again.")