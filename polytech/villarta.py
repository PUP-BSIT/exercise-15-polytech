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
        pass

    def input_profile(self):
        pass

    def show_menu(self):
        pass

    def handle_choice(self, choice):
        pass

    def menu():
        pass
