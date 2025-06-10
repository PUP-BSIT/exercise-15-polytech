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
            "Dog 🐶", "Cat 🐱", "Bird 🐦", "Fish 🐠"
        ]

        print("\nAvailable Species:")
        for i, s in enumerate(species_list, 1):
            print(f"{i}. {s}")
            
        while True:
            sel = input("\nSelect species by number (or 'c' to cancel): ")
            if sel.lower() == 'c':
                print("Species selection canceled.")
                return
            try:
                ch = int(sel)
                if 1 <= ch <= len(species_list):
                    self.species = species_list[ch - 1]
                    print(f"Species selected: {self.species}")
                    return
                else:
                    print(f"Choose a number 1-{len(species_list)}.")
            except ValueError:
                print("Invalid input. Enter a number.")

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
