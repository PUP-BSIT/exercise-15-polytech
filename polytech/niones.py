from colorama import Fore


UNSET_OPTION = '-1'
EXIT_OPTION = '0'


class Profile:
    def __init__(self, name, art_style, tools):
        self.name = name
        self.art_style = art_style
        self.tools = tools

    def display_name(self):
        pass

    def display_art_style(self):
        pass

    def display_tools(self):
        pass

    def display_summary(self):
        pass

    def input_profile(self):
        pass

    def show_menu(self):
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
