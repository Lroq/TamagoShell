import time
from creature.main_creature_menu import MainCreatureMenu
from colorama import Fore, init
from game.game import game

init(autoreset=True)


def display_ascii_art():
    art = [
        "  _______  ",
        " |  ___  | ",
        r" | |   | |  /\_/\  ",
        " | |___| | ( o.o ) ",
        " |_______|  > ^ <  ",
        "  Tamagochi School! ",
    ]

    for line in art:
        print(Fore.YELLOW + line)
        time.sleep(0.1)
    print("\n")


class Menu:
    def __init__(self):
        self.running = True

    def display_menu(self):
        print(Fore.BLUE + "\nBienvenue dans le jeu de Tamagotchi !" + "\n")
        print("1. Jouer")
        print("2. Créer ou charger une créature")
        print("3. Quitter" + "\n")

    def handle_choice(self, choice):
        match choice:
            case "1":
                print("\nLancement du jeu...")
                time.sleep(0.5)
                game()
            case "2":
                MainCreatureMenu().display_menu()
            case "3":
                print("\nMerci d'avoir joué !")
                self.running = False
            case _:
                print(Fore.RED + "Choix invalide, veuillez réessayer.")

    def run(self):
        try:
            display_ascii_art()
            while self.running:
                self.display_menu()
                choice = input(Fore.BLUE + "Quel est votre choix ?" + "\n")
                self.handle_choice(choice)
        except KeyboardInterrupt:
            print("\nFin du programme. Merci d'avoir joué !")
