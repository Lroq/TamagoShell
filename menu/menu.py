import time
import sys
import os
from colorama import Fore, init, Style
from game.game import game
from creature.creature_manager import CreatureManager
from creature.creature_menu import creature_menu

init(autoreset=True)


def display_ascii_art():
    art = [
        "  _______  ",
        " |  ___  | ",
        r" | |   | |  /\_/\  ",
        " | |___| | ( o.o ) ",
        " |_______|  > ^ <  ",
        "  Tamagotchi School! ",
    ]

    for line in art:
        print(Fore.YELLOW + line)
        time.sleep(0.1)
    print("\n")


class Menu:
    def __init__(self):
        self.running = True

    def display_menu(self):
        print(Fore.BLUE + "\nWelcome to the Tamagotchi game!" + "\n")
        print("1. Play, " + Fore.YELLOW + "Your stats decrease automatically even if they don't visibly decrease in real-time.")
        print("2. Create a creature that you can charge when you enter play.")
        print("3. Exit\n")

    def handle_choice(self, choice):
        match choice:
            case "1":
                print("\nStarting the game...")
                time.sleep(0.5)
                game()
            case "2":
                    creature = creature_menu()
                    print(Fore.BLUE + Style.BRIGHT + "\nDo you want to save you creature ?")
                    CreatureManager().save_creature(creature)
                    print(Fore.GREEN + Style.BRIGHT + "Your creature has been saved successfully!")

            case "3":
                print("\nThank you for playing!")
                self.running = False
            case _:
                print(Fore.RED + "Invalid choice, please try again.")

    def run(self):
        try:
            display_ascii_art()
            while self.running:
                self.display_menu()
                try:
                    if sys.stdin.closed:
                        sys.stdin = open(os.devnull)
                    choice = input(Fore.BLUE + "What is your choice?" + "\n")
                except EOFError:
                    print("\nInput stream closed. Exiting.")
                    break
                self.handle_choice(choice)
        except KeyboardInterrupt:
            print("\nProgram terminated. Thank you for playing!")
