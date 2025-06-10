import os
import random
from colorama import Fore, Style, init

init(autoreset=True)

class StudentLifeManager:
    def __init__(self):
        self.student_name = ""
        self.student_school = ""
        self.todo_list = []
        self.quotes = [
            "Keep going, you're doing great!",
            "Believe in yourself and all that you are.",
            "Every day is a new beginning.",
            "Push yourself, because no one else will.",
            "Success comes from daily efforts."
        ]

    def view_profile(self):
        pass

    def add_task(self):
        pass

    def view_tasks(self):
        pass

    def clear_tasks(self):
        pass

    def motivate_me(self):
        pass

    def menu(self):
        print(Fore.YELLOW + Style.BRIGHT + 
              "Welcome to Student Life Manager!\n")
        self.student_name = input(Fore.CYAN + "Enter your name: ").strip()
        self.student_school = input(Fore.CYAN + "Enter your school: ").strip()

        while True:
            print(Fore.YELLOW + Style.BRIGHT + 
                  "==== STUDENT LIFE MANAGER ====")
            print(Fore.CYAN + "1. View Profile")
            print(Fore.CYAN + "2. Add Task")
            print(Fore.CYAN + "3. View Tasks")
            print(Fore.CYAN + "4. Clear Tasks")
            print(Fore.CYAN + "5. Motivate Me")
            print(Fore.CYAN + "6. Back to Main Menu")
            print(Fore.YELLOW + Style.BRIGHT + 
                  "==============================")
            choice = input(Fore.CYAN + "Enter choice: ")

            if choice == '1':
                self.view_profile()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':
                self.clear_tasks()
            elif choice == '5':
                self.motivate_me()
            elif choice == '6':
                print("Goodbye!\n")
                break
            else:
                print("Invalid input. Try again.\n")

            input(Fore.MAGENTA + "Press Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')