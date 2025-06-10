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

    def menu(self):
        while True:
            self.clear_screen()
            print(Fore.MAGENTA + "=" * 55)
            print("\t   ⟡˙⋆ Victorio's Diary System ⋆˙⟡ ")
            print(Fore.MAGENTA + "=" * 55)
            print("[1.]" + Fore.MAGENTA + " Add Mood")
            print("[2.]" + Fore.MAGENTA + " Write Journal Entry")
            print("[3.]" + Fore.MAGENTA + " View Journal Entries")
            print("[4.]" + Fore.MAGENTA + " Delete an Entry")
            print("[5.]" + Fore.MAGENTA + " Show Summary")
            print("[0.]" + Fore.MAGENTA + " Back to Main Menu")
            print(Fore.MAGENTA + "=" * 55)

            choice = input("Enter your choice: ").strip()
            self.clear_screen()

            match choice:
                case "1":
                    self.log_mood()
                case "2":
                    self.add_journal_entry()
                case "3":
                    self.view_entries()
                case "4":
                    self.delete_entry()
                case "5":
                    self.show_summary()
                case "0":
                    print(Fore.CYAN + "Returning to main menu.")
                    break
                case _:
                    print(Fore.RED + "Invalid choice.")
            input("\nPress Enter to continue...")

tracker = WellnessDiary()
tracker.menu()