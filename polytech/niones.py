from colorama import Fore


UNSET_OPTION = '-1'
EXIT_OPTION = '0'


class Profile:
    def __init__(self, name, art_style, tools):
        self.name = name
        self.art_style = art_style
        self.tools = tools

    def display_name(self):
        if not self.name:
            print(Fore.YELLOW + "=" * 50)
            print(" 🎨 INPUT ARTIST NAME 🎨 ")
            print("=" * 50 + Fore.RESET)
            print("\nNo input.")
            return
        print(f"\nArtist Name: {Fore.CYAN}{self.name}{Fore.RESET}")

    def display_art_style(self):
        if not self.art_style:
            print("\nNo input.")
            return
        print(f"\nArt Style: {Fore.CYAN}{self.art_style}{Fore.RESET}")

    def display_tools(self):
        pass

    def display_summary(self):
        pass

    def input_profile(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        return input("\nEnter your choice: ")  # TEMPORARY placeholder

    def handle_choice(self, choice):
        pass


def menu():
    artist = Profile("", "", "")
    artist.input_profile()
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = artist.show_menu()
        artist.handle_choice(choice)


menu()
