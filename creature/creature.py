import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

class Creature:
    def __init__(self, name, species, accessories, health=100, hunger=100, age=1, energy=100, happiness=100, is_alive=True):
        self.name = name
        self.species = species
        self.accessories = accessories
        self.health = health
        self.hunger = hunger
        self.age = age
        self.energy = energy
        self.happiness = happiness
        self.is_alive = is_alive

    def age_up(self):
        self.age += 1
        self.hunger -= 10
        self.energy -= 10
        self.check_status()
        self.evolve()

    def evolve(self):
        if self.age % 5 == 0:
            print(Fore.GREEN + Style.BRIGHT + f"{self.name} is evolving!")

    def random_event(self):
        events = [
            ("found food", {"hunger": 20}),
            ("took a nap", {"energy": 15}),
            ("had a bad dream", {"health": -10}),
            ("played a game", {"happiness": 10}),
            ("caught a cold", {"health": -15}),
        ]
        event, effect = random.choice(events)
        print(Fore.YELLOW + Style.BRIGHT + f"An event occurred: {event}")
        time.sleep(3)
        for stat, value in effect.items():
            setattr(self, stat, max(0, min(100, getattr(self, stat) + value)))
        self.check_status()

    def check_status(self):
        if self.health <= 0 or self.hunger <= 0:
            self.is_alive = False
            print(Fore.RED + Style.BRIGHT + f"{self.name} has passed away...")

    def display(self):
        stats_text = f"Health: {self.health}/100 | Hunger: {self.hunger}/100 | Age: {self.age} | Energy: {self.energy}/100 | Happiness: {self.happiness}/100"
        print(Fore.BLUE + Style.BRIGHT + "Name:", self.name)
        print(Fore.BLUE + Style.BRIGHT + "Species:", self.species)
        print(Fore.BLUE + Style.BRIGHT + "Accessories:", ", ".join(self.accessories))
        print(Fore.BLUE + Style.BRIGHT + "Stats:", stats_text)