import os
from colorama import Fore, Style, init

init(autoreset=True)

UNSET_OPTION = '-1'
EXIT_OPTION = '0'
LINE_WIDTH = 40

class ProfileInformation:
    def __init__(self, name="", hobbies="", nationality=""):
        self.name = name
        self.hobbies = hobbies
        self.nationality = nationality

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def input_profile(self):
        self.clear_screen()
        print(Fore.WHITE + "=" * LINE_WIDTH)
        print(Fore.YELLOW + " \tENTER PROFILE INFORMATION\n")
        print(Fore.WHITE + "=" * LINE_WIDTH)
        self.name = input("Name: ")
        self.hobbies = input("Hobbies (comma-separated): ")
        self.nationality = input("Nationality: ")

    def display_name(self):
        if not self.name:
            print(Fore.YELLOW + "=" * LINE_WIDTH)
            print(" INPUT NAME ")
            print("=" * LINE_WIDTH)
            print("\nNo name provided.")
            return
        print(f"\nName: {Fore.CYAN}{self.name}")

    def display_hobbies(self):
        if not self.hobbies:
            print("\nNo hobbies provided.")
            return
        print(f"\nHobbies: {Fore.CYAN}{self.hobbies}")

    def display_nationality(self):
        if not self.nationality:
            print("\nNo nationality provided.")
            return
        print(f"\nNationality: {Fore.CYAN}{self.nationality}")

    def display_summary(self):
        print(Fore.YELLOW + "=" * LINE_WIDTH)
        print("     PERSONAL PROFILE")
        print("=" * LINE_WIDTH)

        if not (self.name and self.hobbies and self.nationality):
            print(" Please complete your profile first.")
            return

        print(f"{Fore.CYAN}Name       :{self.name}")
        print(f"{Fore.CYAN}Hobbies    :{self.hobbies}")
        print(f"{Fore.CYAN}Nationality:{self.nationality}")
        print(Fore.YELLOW + "=" * LINE_WIDTH)

    def clear_profile(self):
        self.name = ""
        self.hobbies = ""
        self.nationality = ""
        print(Fore.LIGHTRED_EX + "\nProfile has been cleared.")

    def show_menu(self):
        self.clear_screen()
        print(Fore.WHITE + "=" * LINE_WIDTH)
        print(Fore.YELLOW + "    PROFILE MENU\n")
        print(Fore.WHITE + "=" * LINE_WIDTH)
        print("1 - Input Your Profile")
        print("2 - Show Name")
        print("3 - Show Hobbies")
        print("4 - Show Nationality")
        print("5 - Show Profile Summary")
        print("6 - Delete Profile Details")
        print("0 - Exit")
        return input("\nEnter your choice: ")

    def handle_choice(self, choice):
        self.clear_screen()
        match choice:
            case "1":
                self.input_profile()
                input("\nProfile updated! Press Enter to continue.")
            case "2":
                self.display_name()
                input("\nPress Enter to continue.")
            case "3":
                self.display_hobbies()
                input("\nPress Enter to continue.")
            case "4":
                self.display_nationality()
                input("\nPress Enter to continue.")
            case "5":
                self.clear_screen()
                self.display_summary()
                input("\nPress Enter to continue.")
            case "6":
                self.clear_profile()
                input("\nPress Enter to continue.")
            case "0":
                print(Fore.MAGENTA + "\nExiting program...")
                print("Thank you for using the profile app!")
                print("Goodbye! 👋")
            case _:
                input("\nInvalid choice. Try again.")

    def menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.show_menu()
            self.handle_choice(choice)
