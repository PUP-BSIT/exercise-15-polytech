import os
import random
import pyttsx3
from colorama import Fore, Style, Back, init

init(autoreset=True)  

EXIT_OPTION = "7"
DISPLAY_WIDTH = 30
POEM_SPEECH_RATE = 130
BACK_COMMAND = "back"

class Pet:
    SPECIES_DICT = {
        "Dog": "🐶",
        "Cat": "🐱",
        "Bird": "🐦",
        "Fish": "🐠"
    }

    PERSONALITIES = [
        "Adventurous", "Calm", "Playful", "Shy", "Curious", 
        "Loyal", "Grumpy", "Affectionate", "Energetic", "Goofy",
        "Brave", "Gentle", "Mischievous", "Sassy", "Wise"
    ]

    def __init__(self):
        self.name = ""
        self.species = ""
        self.personality = ""

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def choose_species(self):
        self.clear_screen()

        print("\nAvailable Species:")
        for species_index, (species_name, species_emoji) in enumerate(
            Pet.SPECIES_DICT.items(), start=1
        ):
            print(f"{species_index}. {species_name} {species_emoji}")

        while True:
            selection = input(
                f"\nSelect a species by number\n"  
                f"(or type '{BACK_COMMAND}' to cancel): " 
            )
            if selection.lower() == BACK_COMMAND:
                self.clear_screen() 
                print("\nSpecies selection canceled.")
                return

            try:
                choice_number = int(selection)
            except ValueError:
                self.clear_screen()

                print("\nAvailable Species:")
                for species_index, (species_name, species_emoji) in enumerate(
                    Pet.SPECIES_DICT.items(), start=1
                ):
                    print(f"{species_index}. {species_name} {species_emoji}")
                print("\nInvalid input. Please enter a valid number.") 
                continue

            if not (1 <= choice_number <= len(Pet.SPECIES_DICT)):
                self.clear_screen() 

                print("\nAvailable Species:") 
                for species_index, (species_name, species_emoji) in enumerate(
                    Pet.SPECIES_DICT.items(), start=1
                ):
                    print(f"{species_index}. {species_name} {species_emoji}")
                print( 
                    f"\nInvalid selection. Please enter a number "
                    f"between 1 and {len(Pet.SPECIES_DICT)}"
                )
                continue

            selected_species = list(Pet.SPECIES_DICT.keys())[choice_number - 1]
            selected_emoji = Pet.SPECIES_DICT[selected_species]
            self.species = f"{selected_species} {selected_emoji}"
            self.clear_screen()
            print(f"\nSpecies selected: {self.species}")
            return
        
    def set_pet_name(self):
        if not self.species:
            print("You haven't selected a species yet!")
            response = input(
                f"Select a species first or type '{BACK_COMMAND}' to return: "
            )
            if response.lower() == BACK_COMMAND:
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
                f"(or type '{BACK_COMMAND}' to return): "
            ).strip().title()

            if name_input.lower() == BACK_COMMAND:
                return
            elif not name_input:
                print("Name cannot be empty! Please enter a valid name.")
                continue
            else:
                self.name = name_input
                print(f"Pet name set to: {self.name}")
                break

    def discover_pet_personality(self):
        if not self.species:
            print("You haven't selected a species yet!")
            response = input(
                f"Select a species first or type '{BACK_COMMAND}' to return: "
            )
            if response.lower() == BACK_COMMAND:
                return
            else:
                self.choose_species()
                if not self.species:
                    return

        if not self.name:
            print("Your pet needs a name before discovering its personality!")
            response = input(
                f"Set a name first or type '{BACK_COMMAND}' to return: "
            )
            if response.lower() == BACK_COMMAND:
                return
            else:
                self.set_pet_name()
                if not self.name:
                    return

        self.personality = random.choice(self.PERSONALITIES)
        self.clear_screen()
        msg = (
            f"\n✨ {self.name} the {self.species.split()[0]} is feeling "
            f"quite {self.personality.lower()} today! ✨"
        )
        print(msg[:80])
        print(f"Personality discovered: {self.personality}")

    def display_full_details(self):
        print("\n---- Current Pet Details ----")
        print(f"Pet Name   : {self.name}")
        print(f"Species    : {self.species}")
        print(f"Personality: {self.personality}")
        print("------------------------------")
        
        if self.species:
            print(f"\nYey you got {self.species}!")
        if self.personality:
            print(f"And it has a {self.personality.lower()} personality!")
    
    def recite_pet_poem(self):
        if not (self.name and self.species and self.personality):
            print(
                "\nPlease set pet name, species, and "
                "discover its personality first."
            )
            return  
        
        species_base = self.species.split()[0]

        poem_templates = [
            f"🌟 {self.name}, the {self.species},\n"
            f"With a spirit so {self.personality.lower()},\n"
            "Brings joy with every glance,\n"
            "A true friend, a happy chance.",

            f"🌟 {self.name} watches, {self.personality.lower()} and keen,\n"
            f"A {self.species}, a vibrant scene,\n"
            "Wiser than one might surmise,\n"
            "Reflected in their gentle eyes.",

            f"🌟 Through sun and rain, their mood may shift,\n"
            f"{self.name} the {self.species}, a precious gift,\n"
            f"A {self.personality.lower()} heart, loyal and true,\n"
            "Always there for me and you.",

            f"🌟 Small paws or fins, it matters not,\n"
            f"For {self.name}'s {self.personality.lower()} soul is sought,\n"
            f"This {self.species}, a character grand,\n"
            "The finest spirit in the land.",

            f"🌟 When days are dark or spirits low,\n"
            f"{self.name}'s {self.personality.lower()} nature starts to glow,\n"
            f"This {self.species}'s love, a guiding light,\n"
            "Making everything feel bright."
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
        self.personality = "" 
       
        if not silent:
            print("\nPet details have been cleared.")

    def show_menu(self):
        self.clear_screen()
        print(Back.YELLOW + " " * DISPLAY_WIDTH)
        print(
           Back.YELLOW + " "
           + Style.RESET_ALL
           + Fore.YELLOW
           + Style.BRIGHT
           + "--------- Pet Menu ---------"
           + Back.YELLOW
           + " "
        )
        print("=" * DISPLAY_WIDTH)
        print(" Manage your pet details here. ")
        print("[1] Choose Species")
        print("[2] Set Pet Name")
        print("[3] Discover Pet Personality") 
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
                self.discover_pet_personality() 
            case "4":
                self.display_full_details() 
            case "5":
                self.recite_pet_poem()  
            case "6":
                self.clear_pet_details()
            case _:
                print("Invalid choice. Please try again.")
                
    def menu(self):
        choice = ""
        while choice != EXIT_OPTION:
            choice = self.show_menu()

            if choice == EXIT_OPTION:
                self.clear_screen() 
                print("Exiting Pet Menu...") 
                break

            self.handle_choice(choice)
            input("Press Enter to continue.")
