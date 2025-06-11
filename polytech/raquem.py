import os
import random
import pyttsx3
from colorama import Fore, Style, Back, init

init(autoreset=True)  

EXIT_OPTION = "7"
DISPLAY_WIDTH = 30
POEM_SPEECH_RATE = 130

class Pet:
    
    SPECIES_DICT = {
        "Dog": "🐶",
        "Cat": "🐱",
        "Bird": "🐦",
        "Fish": "🐠"
    }

    def __init__(self):
        self.name = ""
        self.species = ""
        self.age = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def choose_species(self):
        self.clear_screen()
        print("\nAvailable Species:")
        
        for i, (species, emoji) in enumerate(
            Pet.SPECIES_DICT.items(), start=1
        ):
            print(f"{i}. {species} {emoji}")

        while True:
            selection = input(
                "\nSelect a species by number (or 'c' to cancel): "
            )
            if selection.lower() == 'c':
                self.clear_screen() 
                print("\nSpecies selection canceled.")
                return

            try:
                choice = int(selection)
            except ValueError:
                self.clear_screen()
                print("\nAvailable Species:")
                 
                for i, (species_item, emoji_item) in enumerate(
                    Pet.SPECIES_DICT.items(), start=1
                ):
                    print(f"{i}. {species_item} {emoji_item}")
                print("\nInvalid input. Please enter a valid number.") 
                continue

            if not (1 <= choice <= len(Pet.SPECIES_DICT)):
                self.clear_screen() 
                print("\nAvailable Species:") 
                for i, (species_item, emoji_item) in enumerate(
                    Pet.SPECIES_DICT.items(), start=1
                ):
                    print(f"{i}. {species_item} {emoji_item}")
                print( 
                    f"\nInvalid selection. Please enter a number "
                    f"between 1 and {len(Pet.SPECIES_DICT)}"
                )
                continue

            species = list(Pet.SPECIES_DICT.keys())[choice - 1]
            emoji = Pet.SPECIES_DICT[species]
            self.species = f"{species} {emoji}"
            self.clear_screen()
            print(f"\nSpecies selected: {self.species}")
            return
        
    def set_pet_name(self):
        if not self.species:
            print("You haven't selected a species yet!")
            response = input(
                "Select a species first or type 'back' to return: "
            )
            if response.lower() == 'back':
                return
            else:
                self.choose_species()
                if not self.species:
                    return

        species_text = (
            self.species.split()[0] if self.species else "pet"
        )

        while True:
            name_input = input(
                f"Enter the name of your {species_text} "
                "(or type 'back' to return): "
            ).strip().title()

            if name_input.lower() == 'back':
                return
            elif not name_input:
                print("Name cannot be empty! Please enter a valid name.")
                continue
            else:
                self.name = name_input
                print(f"Pet name set to: {self.name}")
                break

    def set_pet_age(self):
        if not self.species:
            print("You haven't selected a species yet!")
            response = input(
                "Select a species first or type 'back' to return: "
            )
            if response.lower() == 'back':
                return
            else:
                self.choose_species()
                if not self.species:
                    return

        species_text = (
            self.species.split()[0] if self.species else "pet"
        )
        while True:
            age_input = input(
                f"Enter the age for your {species_text} "
                "(or type 'back' to return): "
            )
            if age_input.lower() == 'back':
                return
            try:
                self.age = int(age_input)
                print(f"Pet age set to: {self.age}")
                break
            except ValueError:
                self.clear_screen()
                print("Invalid input. Please enter a numeric age.")
                if self.name:
                    print(f"Pet Name: {self.name}")

    def display_full_details(self):
        print("\n---- Current Pet Details ----")
        print(f"Pet Name   : {self.name}")
        print(f"Species    : {self.species}")
        print(f"Age        : {self.age}")
        print("------------------------------")
        
        if self.species:
            print(f"\nYey you got {self.species}!")
    
    def recite_pet_poem(self):
        if not self.name or not self.species:
            print("\nPlease set pet name and species first.")
            return
        
        species_base = self.species.split()[0]

        def year_word(age):
            return "years" if age != 1 else "year"
        
        poem_templates = [
            f"🌟 {self.name}, the {self.species},\n"
            f"With wisdom of {self.age} {year_word(self.age)},\n"
            "Brings joy to all who know them,\n"
            "And calms our deepest fears.",

            f"🌟 {self.name} watches with eyes so keen,\n"
            f"A {self.species} aged just {self.age} {year_word(self.age)},\n"
            "Yet wiser than many have been,\n"
            "A friend for every stage.",

            f"🌟 Through {self.age} {year_word(self.age)} of sun and rain,\n"
            f"{self.name} the {self.species} stands true,\n"
            "A loyal companion without complaint,\n"
            "A heart so pure and true.",

            f"🌟 Small paws or fins, it matters not,\n"
            f"For {self.name}'s soul is grand,\n"
            f"At {self.age} {year_word(self.age)}, this {self.species},\n"
            "Is the finest in the land.",

            f"🌟 When days are dark and spirits low,\n"
            f"{self.name} is there to show,\n"
            f"That {self.age} {year_word(self.age)} of {self.species} love,\n"
            "Is all one needs to grow."
        ]

        poem_text = random.choice(poem_templates)

        print("\n--- Pet Poem ---")
        print(poem_text)
        print("---------------")

        text_for_speech = poem_text.replace("🌟", "")
        
        text_for_speech = text_for_speech.replace(self.species, species_base)
        
        for emoji in Pet.SPECIES_DICT.values():
            text_for_speech = text_for_speech.replace(emoji, "")
      
        try:
            print("\nReciting poem...")
            engine = pyttsx3.init()
            
            engine.setProperty('rate', POEM_SPEECH_RATE)
            
            voices = engine.getProperty('voices')
            if voices:
                engine.setProperty('voice', voices[0].id)
                
            engine.say(text_for_speech)
            engine.runAndWait()
            print("Poem finished!")
        except Exception as e:
            print(f"Error with text-to-speech: {e}")

    def clear_pet_details(self, silent=False):
        self.name = ""
        self.species = ""
        self.age = 0
       
        if not silent:
            print("\nPet details have been cleared.")

    def show_menu(self):
        self.clear_screen()
        print(Back.YELLOW + " " * DISPLAY_WIDTH)
        print(Back.YELLOW + " " +
              Back.RESET + Fore.YELLOW + Style.BRIGHT + "--------- Pet Menu ---------" +
              Back.YELLOW + " "
              )
        print("=" * DISPLAY_WIDTH)
        print(" Manage your pet details here. ")
        print("[1] Choose Species")
        print("[2] Set Pet Name")
        print("[3] Set Pet Age")
        print("[4] Display Pet Details")
        print("[5] Pet Poem") 
        print("[6] Clear Pet Details") 
        print(f"[{EXIT_OPTION}] Exit")  
        print(Back.YELLOW + " " * DISPLAY_WIDTH)
        choice = input("Enter your choice: ")
        return choice
    
    def handle_choice(self, choice):
        self.clear_screen()
        match choice:
            case "1":
                self.choose_species()
            case "2":
                self.set_pet_name()
            case "3":
                self.set_pet_age()
            case "4":
                self.display_full_details() 
            case "5":
                self.recite_pet_poem()  
            case "6":
                self.clear_pet_details()
            case _:
                print("Invalid choice. Please try again.")

    @staticmethod
    def menu():
        pet = Pet()
        choice = ""
        while choice != EXIT_OPTION:
            choice = pet.show_menu()
            if choice == EXIT_OPTION:
                print("Exiting Pet Menu...") 
                break
            pet.handle_choice(choice)
            input("Press Enter to continue.")
        
        pet.clear_screen() 
    
Pet.menu()
