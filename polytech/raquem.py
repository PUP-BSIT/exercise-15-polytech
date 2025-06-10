import os

class Pet:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.age = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

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

    @staticmethod
    def menu():
        pet = Pet()
        choice = ""
        while choice != "0":  
            choice = pet.show_menu()
            print("Option selected:", choice)
            input("\nPress Enter to continue...")

Pet.menu()
