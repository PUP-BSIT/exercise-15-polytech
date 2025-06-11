from colorama import Fore, Style
import os

UNSET_OPTION = '-1'
EXIT_OPTION = '0'

class Profile:
    def __init__(self, name, hobbies, nationality):
        self.name = name
        self.hobbies = hobbies
        self.nationality = nationality

    def display_name(self):
        if not self.name:
            print(Fore.YELLOW + "-" * 40 + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + " No name provided." + Fore.RESET)
            return
        print(f"\n{Fore.LIGHTBLUE_EX}Name:{Fore.RESET} {self.name}")

    def display_hobbies(self):
        if not self.hobbies:
            print(Fore.YELLOW + "\nNo hobbies provided." + Fore.RESET)
            return
        print(f"\n{Fore.LIGHTBLUE_EX}Hobbies:{Fore.RESET} {self.hobbies}")

    def display_nationality(self):
        if not self.nationality:
            print(Fore.YELLOW + "\nNo nationality provided." + Fore.RESET)
            return
        print(f"\n{Fore.LIGHTBLUE_EX}Nationality:{Fore.RESET} "
              f"{self.nationality}")

    def display_summary(self):
        print(Fore.WHITE + "-" * 40)
        print(Fore.LIGHTBLUE_EX + "   PERSONAL PROFILE SUMMARY")
        print(Fore.WHITE + "-" * 40 + Fore.RESET)

        if not self.name or not self.hobbies or not self.nationality:
            print(Fore.LIGHTYELLOW_EX +
                  " Please complete your profile first." + Fore.RESET)
            return

        print(f"{Fore.LIGHTBLUE_EX}Name       :{Fore.RESET} {self.name}")
        print(f"{Fore.LIGHTBLUE_EX}Hobbies    :{Fore.RESET} {self.hobbies}")
        print(f"{Fore.LIGHTBLUE_EX}Nationality:{Fore.RESET} "
              f"{self.nationality}")
        print(Fore.WHITE + "-" * 40 + Fore.RESET)

    def input_profile(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.WHITE + "-" * 40)
        print(Fore.LIGHTBLUE_EX + "   ENTER PROFILE INFORMATION")
        print(Fore.WHITE + "-" * 40 + Fore.RESET)
        self.name = input("Name: ")
        self.hobbies = input("Hobbies (comma-separated): ")
        self.nationality = input("Nationality: ")

    def show_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.WHITE + "-" * 40)
        print(Fore.LIGHTBLUE_EX + "        PROFILE MENU")
        print(Fore.WHITE + "-" * 40 + Fore.RESET)
        print("1 - Show Name")
        print("2 - Show Hobbies")
        print("3 - Show Nationality")
        print("4 - Show Profile Summary")
        print("5 - Update Profile")
        print("0 - Exit")
        return input("\nChoose an option: ")

    def handle_choice(self, choice):
        match choice:
            case '1':
                self.display_name()
                input("\nPress Enter to continue.")
            case '2':
                self.display_hobbies()
                input("\nPress Enter to continue.")
            case '3':
                self.display_nationality()
                input("\nPress Enter to continue.")
            case '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.display_summary()
                input("\nPress Enter to continue.")
            case '5':
                self.input_profile()
                input("\nProfile updated! Press Enter to continue.")
            case '0':
                print(Fore.LIGHTMAGENTA_EX +
                      "\nExiting... Thank you for using the profile app!" +
                      Fore.RESET)
            case _:
                input(Fore.RED + "\nInvalid choice. Try again." + Fore.RESET)

def profile_menu():
    user = Profile("", "", "")
    user.input_profile()
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = user.show_menu()
        user.handle_choice(choice)

profile_menu()
