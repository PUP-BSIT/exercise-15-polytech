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
                input("Press Enter to continue.")
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
            input("Press Enter to continue.")
            return

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
                pass
            case "3":
                pass
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

Pet.menu()
