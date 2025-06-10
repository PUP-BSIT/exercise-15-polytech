import os
from colorama import init, Fore

EXIT_OPTION = 0

init(autoreset = True)

class WellnessDiary:
    def __init__(self):
        self.username = "Anonymous"
        self.mood = "Neutral"
        self.journal_entries = []

    def log_mood(self):
        print(Fore.MAGENTA + "=" * 55)
        print(" \t\tLog your current Mood")
        print(Fore.MAGENTA + "=" * 55)
        mood = input("How are you feeling today?"
                     " (e.g., Happy, Sad, Anxious): ")
        self.mood = mood
        print(Fore.GREEN + f"Mood updated to: {self.mood}")

    def add_journal_entry(self):
        print(Fore.MAGENTA + "=" * 55)
        print(" \t\tAdd Journal Entry")
        print(Fore.MAGENTA + "=" * 55)
        date = input("Enter date (YYYY-MM-DD): ")
        entry = input("Write your journal entry: ")
        dated_entry = f"[{date}] {entry}"
        self.journal_entries.append(dated_entry)
        print(Fore.GREEN + "Journal entry added.")

    def view_entries(self):
        print(Fore.MAGENTA + "=" * 55)
        print(" \t\tView Journal Entries")
        print(Fore.MAGENTA + "=" * 55)
        if not self.journal_entries:
            print(Fore.YELLOW + "No journal entries yet.")
            return

        for i, entry in enumerate(self.journal_entries, 1):
            print(f"{i}. {entry}")

    def delete_entry(self):
        print(Fore.MAGENTA + "=" * 55)
        print(" \tDelete Journal Entry")
        print(Fore.MAGENTA + "=" * 55)

        if not self.journal_entries:
            print(Fore.YELLOW + "No entries to delete.")
            return

        for i, entry in enumerate(self.journal_entries, 1):
            print(f"{i}. {entry}")

        try:
            choice = int(input(Fore.RED + "Enter entry number to delete: "))
            removed_entry = self.journal_entries.pop(choice - 1)
            print(Fore.GREEN + f"Deleted: {removed_entry}")
        except:
            print(Fore.RED + "Invalid input or number.")

    def show_summary(self):
        print(Fore.MAGENTA + "=" * 55)
        print(" \tVictorio's Mental Health Summary ")
        print(Fore.MAGENTA + "=" * 55)
        print(f"Username:                   {self.username}")
        print(f"Current Mood:               {self.mood}")
        print(f"Total Journal Entries:      {len(self.journal_entries)}")


tracker = WellnessDiary()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print(Fore.MAGENTA + "=" * 55)
    print( "\t   ⟡˙⋆ Victorio's Diary System ⋆˙⟡ ")
    print(Fore.MAGENTA + "=" * 55)
    print("[1.]" + Fore.MAGENTA + " Add Mood")
    print("[2.]" + Fore.MAGENTA + " Write Journal Entry")
    print("[3.]" + Fore.MAGENTA + " View Journal Entries")
    print("[4.]" + Fore.MAGENTA + " Delete an Entry")
    print("[5.]" + Fore.MAGENTA + " Show Summary")
    print("[0.]" + Fore.MAGENTA + " Back to Main Menu")
    print(Fore.MAGENTA + "=" * 55)

def process_choice(choice):
    clear_screen()
    match choice:
        case 1:
            tracker.log_mood()
        case 2:
            tracker.add_journal_entry()
        case 3:
            tracker.view_entries()
        case 4:
            tracker.delete_entry()
        case 5:
            tracker.show_summary()
        case _:
            print(Fore.RED + "Invalid choice. Try again.")
    input("\nPress Enter to Continue...")

def get_user_choice():
    try:
        return int(input(Fore.MAGENTA + "Enter your choice: "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
        return None

def menu():
    while True:
        clear_screen()
        display_menu()
        choice = get_user_choice()
        if choice is None:
            input("Press Enter to continue...")
            continue

        if choice == EXIT_OPTION:
            print(Fore.CYAN + "Going back to Main Menu.")
            break

        process_choice(choice)

menu()