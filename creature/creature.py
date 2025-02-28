import shutil
from colorama import Fore, Style, init

init(autoreset=True)


class Creature:
    def __init__(self, name, species, accessories, health=100, hunger=100, age=1, is_alive=True, energy=100, happiness=100, sanity=100):
        self.name = name
        self.species = species
        self.accessories = accessories
        self.health = health
        self.hunger = hunger
        self.age = age
        self.energy = energy
        self.happiness = happiness
        self.sanity = sanity
        self.is_alive = is_alive

    def display(self):
        stats_text = f"Health: {self.health}\\100 | Hunger: {self.hunger}\\100 | Age: {self.age} | Energy: {self.energy}\\100 | Happiness: {self.happiness}\\100 | Sanity: {self.sanity}\\100\n"

        print(Fore.BLUE + Style.BRIGHT + "Name:", self.name)
        print(Fore.BLUE + Style.BRIGHT + "Species:", self.species)
        print(Fore.BLUE + Style.BRIGHT + "Accessories:", ", ".join(self.accessories))
        print(Fore.BLUE + Style.BRIGHT + "Stats:", stats_text)
