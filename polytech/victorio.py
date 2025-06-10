EXIT_OPTION = 0

def display_menu():
    print("=" * 55)
    print("\t   ⟡˙⋆ Victorio's Diary System ⋆˙⟡ ")
    print("=" * 55)
    print("[1.] Add Mood")
    print("[2.] Write Journal Entry")
    print("[3.] View Journal Entries")
    print("[4.] Delete an Entry")
    print("[5.] Show Summary")
    print("[0.] Back to Main Menu")
    print("=" * 55)

def process_choice(choice):
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
            print("Invalid choice. Try again.")
    input("\nPress Enter to Continue...")

def get_user_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def kalelle():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == EXIT_OPTION:
            print("Going back to Main Menu.")
            break
        elif 1 <= choice <= 5:
            process_choice(choice)
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")

kalelle()