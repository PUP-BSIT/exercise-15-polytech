import os
from polytech import raquem

EXIT_OPTION = 6
UNSET_OPTION = -1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("================================")
    print("      PolyTech Menu System      ")
    print("================================")
    print("1. Annie Rose Raquem's Pet Module")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Exit")
    print("================================")

def get_user_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return UNSET_OPTION

def display_get_choice(choice):
    match choice:
        case 1:
            raquem.Pet.menu()
        case 2:
            #TO-DO(Victorio): call your module here
            pass
        case 3:
            #TO-DO(Capilitan): call your module here
            pass
        case 4:
            #TO-DO(Niones): call your module here
            pass
        case 5:
            #TO-DO(Villarta): call your module here
            pass
        case _:
            print("Invalid choice. Try again.")
            
def main():
    while True:
        clear_screen()
        display_menu()
        choice = get_user_choice()

        if choice == EXIT_OPTION:
            print("Exiting the system.")
            break
        elif 1 <= choice <= 5:
            clear_screen()
            display_get_choice(choice)
            input("Press Enter to continue...")
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")

main()