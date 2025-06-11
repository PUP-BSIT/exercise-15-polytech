import os
from colorama import init, Fore

EXIT_OPTION = 0
LINE_WIDTH = 55

init(autoreset = True)

class WellnessDiary:
    def __init__(self):
        self.username = "Anonymous"
        self.mood = "Neutral"
        self.journal_entries = []

    def line_design(self, color=Fore.MAGENTA):
        print(color + "=" * LINE_WIDTH)

    def log_mood(self):
        self.line_design()
        print(" \t\tLog your current Mood")
        self.line_design()
        mood = input("How are you feeling today?"
                     " (e.g., Happy, Sad, Anxious): ")
        self.mood = mood
        print(Fore.GREEN + f"Mood updated to: {self.mood}")

    def add_journal_entry(self):
        self.line_design()
        print(" \t\tAdd Journal Entry")
        self.line_design()
        entry = input("Write your journal entry: ")
        self.journal_entries.append(entry)
        print(Fore.GREEN + "Journal entry added.")

    def view_entries(self):
        self.line_design()
        print(" \t\tView Journal Entries")
        self.line_design()
        if not self.journal_entries:
            print(Fore.YELLOW + "No journal entries yet.")
            return

        for index, entry in enumerate(self.journal_entries, 1):
            print(f"{index}. {entry}")

    def delete_entry(self):
        self.line_design()
        print(" \tDelete Journal Entry")
        self.line_design()

        if not self.journal_entries:
            print(Fore.YELLOW + "No entries to delete.")
            return

        for index, entry in enumerate(self.journal_entries, 1):
            print(f"{index}. {entry}")

        try:
            choice = int(input(Fore.RED + "Enter entry number to delete: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            return

        if choice < 1 or choice > len(self.journal_entries):
            print(Fore.RED + "Entry number is out of range.")
            return

        removed_entry = self.journal_entries.pop(choice - 1)
        print(Fore.GREEN + f"Deleted: {removed_entry}")

    def show_summary(self):
        self.line_design()
        print(" \t Victorio's Mental Health Summary ")
        self.line_design()
        print(f"Username:                       {self.username}")
        print(f"Current Mood:                   {self.mood}")
        print(f"Total Journal Entries:          {len(self.journal_entries)}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        self.line_design()
        print( "\t   ⟡˙⋆ Victorio's Diary System ⋆˙⟡ ")
        self.line_design()
        print("[1.]" + Fore.MAGENTA + " Add Mood")
        print("[2.]" + Fore.MAGENTA + " Write Journal Entry")
        print("[3.]" + Fore.MAGENTA + " View Journal Entries")
        print("[4.]" + Fore.MAGENTA + " Delete an Entry")
        print("[5.]" + Fore.MAGENTA + " Show Summary")
        print("[0.]" + Fore.MAGENTA + " Back to Main Menu")
        self.line_design()

    def process_choice(self, choice):
        self.clear_screen()
        match choice:
            case 1:
                self.log_mood()
            case 2:
                self.add_journal_entry()
            case 3:
                self.view_entries()
            case 4:
                self.delete_entry()
            case 5:
                self.show_summary()
            case _:
                print(Fore.RED + "Invalid choice. Try again.")
        input("\nPress Enter to Continue...")

    def get_user_choice(self):
        try:
            return int(input(Fore.MAGENTA + "Enter your choice: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            return None

    def menu(self):
        #display menu until user chooses 0
        while True:
            self.clear_screen()
            self.display_menu()
            choice = self.get_user_choice()
            if choice is None:
                input("Press Enter to continue...")
                continue

            if choice == EXIT_OPTION:
                print(Fore.CYAN + "Going back to Main Menu.")
                break

            self.process_choice(choice)