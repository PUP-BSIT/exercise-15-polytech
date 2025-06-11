from colorama import Fore
import os

UNSET_OPTION = '-1'
EXIT_OPTION = '0'
LINE_WIDTH = 50

class Profile:
    def __init__(self, name, art_style, tools):
        self.name = name
        self.art_style = art_style
        self.tools = tools

    def display_name(self):
        if not self.name:
            print(Fore.YELLOW + "=" * LINE_WIDTH)
            print(" 🎨 INPUT ARTIST NAME 🎨 ")
            print("=" * LINE_WIDTH + Fore.RESET)
            print("\nNo input.")
            return
        print(f"\nArtist Name: {Fore.CYAN}{self.name}{Fore.RESET}")

    def display_art_style(self):
        if not self.art_style:
            print("\nNo input.")
            return
        print(f"\nArt Style: {Fore.CYAN}{self.art_style}{Fore.RESET}")

    def display_tools(self):
        if not self.tools:
            print("\nNo input.")
            return
        print(f"\nFavorite Tools: {Fore.CYAN}{self.tools}{Fore.RESET}")

    def display_summary(self):
        print(Fore.YELLOW + "=" * LINE_WIDTH)
        print("        🎨 ARTIST PROFILE 🎨")
        print("=" * LINE_WIDTH + Fore.RESET)

        if not self.name or not self.art_style or not self.tools:
            print(" Please complete your artist profile first.")
            return

        print(f"{Fore.CYAN}Name        :{Fore.RESET} {self.name}")
        print(f"{Fore.CYAN}Art Style   :{Fore.RESET} {self.art_style}")
        print(f"{Fore.CYAN}Tools       :{Fore.RESET} {self.tools}")
        print(Fore.YELLOW + "=" * LINE_WIDTH + Fore.RESET)

    def input_profile(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.WHITE + "=" * LINE_WIDTH)
        print(Fore.YELLOW + " \t\tENTER ARTIST PROFILE\n" + Fore.RESET)
        print(Fore.WHITE + "=" * LINE_WIDTH)
        self.name = input("Artist Name: ")
        self.art_style = input("Preferred Art Style (e.g. digital, watercolor): ")
        self.tools = input("Favorite Tools (comma-separated): ")

    def show_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.WHITE + "=" * LINE_WIDTH)
        print(Fore.YELLOW + " 🎨 \t\tARTIST PROFILE MENU 🎨\n" + Fore.RESET)
        print(Fore.WHITE + "=" * LINE_WIDTH)
        print("1 - Input Artist Profile")
        print("2 - Show Artist Name")
        print("3 - Show Art Style")
        print("4 - Show Favorite Tools")
        print("5 - Show Artist Profile Summary")
        print("0 - Exit")
        return input("\nEnter your choice: ")

    def handle_choice(self, choice):
        match choice:
            case '1':
                self.input_profile()
                input("\nProfile updated! Press Enter to continue.")
            case '2':
                self.display_name()
                input("\nPress Enter to continue.")
            case '3':
                self.display_art_style()
                input("\nPress Enter to continue.")
            case '4':
                self.display_tools()
                input("\nPress Enter to continue.")
            case '5':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.display_summary()
                input("\nPress Enter to continue.")
            case '0':
                print(Fore.MAGENTA + "\nExiting program...")
                print("Thank you for using the artist profile app!")
                print("Goodbye! 🎨✨" + Fore.RESET)
            case _:
                input("\nInvalid choice. Try again.")

    def menu(self):
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.show_menu()
            self.handle_choice(choice)

artist = Profile("", "", "")
