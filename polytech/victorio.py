import os
from colorama import init, Fore

EXIT_OPTION = 0

init(autoreset = True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print(Fore.MAGENTA + "=" * 55)
    print( "   ⟡˙⋆ Victorio's Diary System ⋆˙⟡ ")
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
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            print(Fore.RED + "Invalid choice. Try again.")
    input("\nPress Enter to Continue...")

def get_user_choice():
    try:
        return int(input(Fore.MAGENTA + "Enter your choice: "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")
        return None

def kalelle():
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

kalelle()