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

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
