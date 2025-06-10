import os

UNSET_OPTION = 0
EXIT_OPTION = 6

def clear_screen():
    os.system('cls')

def display_menu():
    print("-----Menu-----")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Exit")

def get_user_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return UNSET_OPTION

def main():
    while True:
        clear_screen()
        display_menu()
        choice = get_user_choice()

        if choice == EXIT_OPTION:
            print("Exiting the system.")
            break
        elif 1 <= choice <= 5:
            print(f"You selected Option {choice}.")
        else:
            print("Invalid choice. Try again.")

        input("Press Enter to continue...")

main()