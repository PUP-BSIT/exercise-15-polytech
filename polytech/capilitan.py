import os
from colorama import Fore, Style, init

init(autoreset=True)

class StudentLifeManager:
    def __init__(self):
        self.student_name = ""
        self.student_school = ""
        self.todo_list = []

    def enter_profile(self):
        self.student_name = input(Fore.CYAN + "Enter your name: ").strip()
        self.student_school = input(Fore.CYAN + "Enter your school: ").strip()
        print(Fore.MAGENTA + "Profile information saved!\n")

    def view_profile(self):
        if not self.student_name or not self.student_school:
            print(Fore.YELLOW + "Please enter your profile first.\n")
            self.enter_profile()

        print(Fore.YELLOW + Style.BRIGHT + "\n--- Student Profile ---")
        print(f"Name   : {self.student_name}")
        print(f"School : {self.student_school}")
        print(f"Tasks  : {len(self.todo_list)} task(s)\n")

    def add_task(self):
        task = input(Fore.CYAN + "Enter a task to add: ").strip()
        if task:
            self.todo_list.append(task)
            print(Fore.MAGENTA + Style.BRIGHT + f"Task '{task}' added!\n")
        else:
            print("No task entered.\n")

    def view_tasks(self):
        print(Fore.YELLOW + Style.BRIGHT + "\n--- Your To-Do List ---")
        if not self.todo_list:
            print("You have no tasks yet.\n")
        else:
            for task_number, task in enumerate(self.todo_list, start=1):
                print(f"{task_number}. {task}")
            print()

    def clear_tasks(self):
        confirm = input(Fore.CYAN + "Clear all tasks? (yes/no): ").lower()
        if confirm == 'yes':
            self.todo_list.clear()
            print(Fore.MAGENTA + Style.BRIGHT + "All tasks cleared.\n")
        else:
            print("Cancelled.\n")

    def edit_task(self):
        self.view_tasks()
        if self.todo_list:
            try:
                task_number = int(input(Fore.CYAN + 
                                        "Enter the task number to edit: "))
                if 1 <= task_number <= len(self.todo_list):
                    new_task = input(Fore.CYAN + 
                                     "Enter the new task: ").strip()
                    if new_task:
                        old_task = self.todo_list[task_number - 1]
                        self.todo_list[task_number - 1] = new_task
                        print(Fore.MAGENTA + Style.BRIGHT + 
                              f"Task '{old_task}' changed to '{new_task}'.\n")
                    else:
                        print("No new task entered.\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + Style.BRIGHT + 
                  "==== STUDENT LIFE MANAGER ====")
            print(Fore.CYAN + "1. Input Profile")
            print(Fore.CYAN + "2. View Profile")
            print(Fore.CYAN + "3. Add Task")
            print(Fore.CYAN + "4. View Tasks")
            print(Fore.CYAN + "5. Clear Tasks")
            print(Fore.CYAN + "6. Edit Task")
            print(Fore.CYAN + "7. Exit")
            print(Fore.YELLOW + Style.BRIGHT + 
                  "==============================")
            choice = input(Fore.CYAN + "Enter choice: ")

            if choice == '1':
                self.enter_profile()
            elif choice == '2':
                self.view_profile()
            elif choice == '3':
                self.add_task()
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                self.clear_tasks()
            elif choice == '6':
                self.edit_task()
            elif choice == '7':
                print("Goodbye!\n")
                break
            else:
                print("Invalid input. Try again.\n")

            input(Fore.MAGENTA + "Press Enter to continue...")