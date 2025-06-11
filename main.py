import os
from polytech.raquem import Pet
from polytech.victorio import WellnessDiary
from polytech.niones import Profile
from polytech.capilitan import StudentLifeManager
from polytech.villarta import ProfileInformation

EXIT_OPTION = 6
UNSET_OPTION = -1
MIN_OPTION = 1
MAX_OPTION = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("================================")
    print("      PolyTech Menu System      ")
    print("================================")
    print("1. Annie Rose Raquem's Pet Module")
    print("2. Kalelle Mae Victorio's Diary Module")
    print("3. Mikee Capilitan's Student Life Manager Module")
    print("4. Zyra Joy Niones' Artist Profile Module")
    print("5. John Keith Villarta's Basic Information Module")
    print("6. Exit")
    print("================================")

def get_user_choice():
    try:
        return int(input("Enter choice: "))
    except ValueError:
        return UNSET_OPTION

def display_and_handle_choice(choice):
    match choice:
        case 1:
            raquem = Pet()
            raquem.menu()
        case 2:
            victorio = WellnessDiary()
            victorio.menu()
        case 3:
            capilitan = StudentLifeManager()
            capilitan.menu()
        case 4:
            niones = Profile("", "", "")
            niones.menu()
        case 5:
            villarta = ProfileInformation("", "", "")
            villarta.menu()
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

        if MIN_OPTION <= choice <= MAX_OPTION:
            clear_screen()
            display_and_handle_choice(choice)
            input("Press Enter to continue...")
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")

main()