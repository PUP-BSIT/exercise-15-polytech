import os

class Pet:
    EXIT_OPTION = "7" 

    def __init__(self):
        self.name = ""
        self.species = ""
        self.age = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def choose_species(self):
        species_list = [
            "Dog 🐶",
            "Cat 🐱",
            "Bird 🐦",
            "Fish 🐠"
        ]
        print("\nAvailable Species:")
        for i, species in enumerate(species_list, start=1):
            print(f"{i}. {species}")

        while True:
            selection = input(
                "\nSelect a species by number (or 'c' to cancel): "
            )
            if selection.lower() == 'c':
                print("\nSpecies selection canceled.")
                return

            try:
                choice = int(selection)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
                continue

            if not (1 <= choice <= len(species_list)):
                print(
                    f"\nInvalid selection. Please enter a number "
                    f"between 1 and {len(species_list)}"
                )
                continue

            self.species = species_list[choice - 1]
            print(f"\nSpecies selected: {self.species}")
            return
        
    def set_pet_name(self):
        if not self.species:
            print("You haven't selected a species yet!")
            response = input(
                "Select a species first or type 'back' to return: "
            )
            if response.lower() == 'back':
                return
            else:
                self.choose_species()
                if not self.species:
                    return

        species_text = (
            self.species.split()[0] if self.species else "pet"
        )

        while True:
            name_input = input(
                f"Enter the name of your {species_text} "
                "(or type 'back' to return): "
            ).strip().title()

            if name_input.lower() == 'back':
                return
            elif not name_input:
                print("Name cannot be empty! Please enter a valid name.")
                continue
            else:
                self.name = name_input
                print(f"Pet name set to: {self.name}")
                break

    def set_pet_age(self):
        if not self.species:
            print("You haven't selected a species yet!")
            response = input(
                "Select a species first or type 'back' to return: "
            )
            if response.lower() == 'back':
                return
            else:
                self.choose_species()
                if not self.species:
                    return

        species_text = (
            self.species.split()[0] if self.species else "pet"
        )
        while True:
            age_input = input(
                f"Enter the age for your {species_text} "
                "(or type 'back' to return): "
            )
            if age_input.lower() == 'back':
                return
            try:
                self.age = int(age_input)
                print(f"Pet age set to: {self.age}")
                break
            except ValueError:
                self.clear_screen()
                print("Invalid input. Please enter a numeric age.")
                if self.name:
                    print(f"Pet Name: {self.name}")

    def show_menu(self):
        self.clear_screen()
        print("\n--- Pet Menu ---")
        print("Manage your pet details here.")
        print("----------------------------")
        print("[1] Choose Species")
        print("[2] Set Pet Name")
        print("[3] Set Pet Age")
        print("----------------------------")
        choice = input("Enter your choice: ")
        return choice
    
    def handle_choice(self, choice):
        os.system('cls' if os.name == 'nt' else 'clear')
        match choice:
            case "1":
                self.choose_species()
            case "2":
                self.set_pet_name()
            case "3":
                self.set_pet_age()
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case Pet.EXIT_OPTION:
                print("Exiting Pet Menu...")
            case _:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue.")

    @staticmethod
    def menu():
        pet = Pet()
        choice = ""
        while choice != Pet.EXIT_OPTION:
            choice = pet.show_menu()
            pet.handle_choice(choice)
            input("Press Enter to continue.")

Pet.menu()
