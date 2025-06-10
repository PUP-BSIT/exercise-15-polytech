from colorama import Fore
import os

UNSET_OPTION = '-1'
EXIT_OPTION = '0'

class Profile:
    def __init__(self, name, age, birthday, hobbies, nationality):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.hobbies = hobbies
        self.nationality = nationality

    def display_name(self):
        if not self.name:
            print("\nNo input.")
            return
        print(f"\nName: {Fore.CYAN}{self.name}{Fore.RESET}")

    def display_age(self):
        if not self.age:
            print("\nNo input.")
            return
        print(f"\nAge: {Fore.CYAN}{self.age}{Fore.RESET}")

    def display_birthday(self):
         if not self.birthday:
            print("\nNo input.")
            return
        print(f"\nBirthday: {Fore.CYAN}{self.birthday}{Fore.RESET}")

    def display_hobbies(self):
        if not self.hobbies:
            print("\nNo input.")
            return
        print(f"\nHobbies: {Fore.CYAN}{self.hobbies}{Fore.RESET}")

    def display_nationality(self):
        if not self.nationality:
            print("\nNo input.")
            return
        print(f"\nNationality: {Fore.CYAN}{self.nationality}{Fore.RESET}")

    def display_summary(self):
        print(Fore.YELLOW + "=" * 40)
        print("        ✨ PERSONAL PROFILE ✨")
        print("=" * 40 + Fore.RESET)

        if (not self.name or not self.age or not self.birthday or 
            not self.hobbies or not self.nationality):
            print(" Please complete your profile details first.")
            return

        print(f"{Fore.CYAN}Name        :{Fore.RESET} {self.name}")
        print(f"{Fore.CYAN}Age         :{Fore.RESET} {self.age}")
        print(f"{Fore.CYAN}Birthday    :{Fore.RESET} {self.birthday}")
        print(f"{Fore.CYAN}Hobbies     :{Fore.RESET} {self.hobbies}")
        print(f"{Fore.CYAN}Nationality :{Fore.RESET} {self.nationality}")
        print(Fore.YELLOW + "=" * 40 + Fore.RESET)

    def input_profile(self):
        os.system('cls')
        print(Fore.YELLOW + " ENTER PERSONAL PROFILE\n" + Fore.RESET)
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.birthday = input("Birthday: ")
        self.hobbies = input("Hobbies (comma-separated): ")
        self.nationality = input("Nationality: ")

    def show_menu(self):
        os.system('cls')
        print(Fore.YELLOW + " PERSONAL PROFILE MENU\n" + Fore.RESET)
        print("1 - Show Name")
        print("2 - Show Age")
        print("3 - Show Birthday")
        print("4 - Show Hobbies")
        print("5 - Show Nationality")
        print("6 - Show Profile Summary")
        print("0 - Exit")
        return input("\nEnter your choice: ")

    def handle_choice(self, choice):
        match choice:
            case '1':
                self.display_name()
                input("\nPress Enter to continue.")
            case '2':
                self.display_age()
                input("\nPress Enter to continue.")
            case '3':
                self.display_birthday()
                input("\nPress Enter to continue.")
            case '4':
                self.display_hobbies()
                input("\nPress Enter to continue.")
            case '5':
                self.display_nationality()
                input("\nPress Enter to continue.")
            case '6':
                os.system('cls')
                self.display_summary()
                input("\nPress Enter to continue.")
            case '0':
                print(Fore.MAGENTA + "\nExiting program...")
                print("Thank you for using the profile app!")
                print("Goodbye! ✨" + Fore.RESET)
            case _:
                input("\nInvalid choice. Try again.")

    def menu():
        pass
