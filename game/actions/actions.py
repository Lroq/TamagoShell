import os
import time
import random
from colorama import Fore, init
from datetime import timedelta

init(autoreset=True)

class Actions:
    def __init__(self):
        self.food = {
            "1": "🍔 Hamburger",
            "2": "🍕 Pizza",
            "3": "🍣 Sushi",
            "4": "🍝 Pasta",
        }

    def eat(self, current_creature):
        print(Fore.BLUE + "\nChoose the food for your creature:")
        print(Fore.BLUE + "--------------------------------------------------------")
        for key, value in self.food.items():
            print(Fore.YELLOW + f"{key}. {value}")
        print(Fore.BLUE + "--------------------------------------------------------")

        choice = input(Fore.GREEN + "What is your choice? \n")
        food = self.food.get(choice)

        if food:
            print(Fore.BLUE + f"\nThe chosen food is {food}, it's a delight\n")
            current_creature.hunger += 10
            self.update_health(10, current_creature)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return food
        else:
            print(Fore.RED + "Invalid choice, please try again.")
            return self.eat(current_creature)

    def sleep(self, current_creature):
        print(Fore.BLUE + "Your creature is now sleeping... 💤")
        self.update_health(20, current_creature)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        current_creature.energy += 10

        # Incrémenter le compteur de sommeil
        if not hasattr(current_creature, 'sleep_count'):
            current_creature.sleep_count = 0
        current_creature.sleep_count += 1

        # 4 dodo tu prends 1 ans
        if current_creature.sleep_count % 4 == 0:
            current_creature.age += 1  # Le sommeil rend la créature plus âgée

        #return 1

    def play(self, current_creature):
        print(Fore.BLUE + "Your creature is now playing. 🎮")
        print(Fore.BLUE + "I am playing...")
        self.update_health(-15, current_creature)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        current_creature.happiness += 10
        current_creature.energy -= 5
    
    def update_health(self, current_creature):
        if current_creature.health > 100:
            current_creature.health = 100
        elif current_creature.health < 0:
            current_creature.health = 0
        print(Fore.CYAN + f"\nCurrent health: {current_creature.health}/100\n")
        if current_creature.health == 0:
            print(Fore.RED + "Your creature is exhausted! It needs rest or food.")


    def go_to_bar(self, current_creature):
        if current_creature.age < 18:
            print(Fore.RED + "Your creature is not old enough to go to the bar... They need to grow up first! 🐣")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        print(Fore.BLUE + "Your creature is heading to the bar... 🍻")
        time.sleep(5)

        if random.randint(1, 5) == 1:
            print(Fore.GREEN + "You met someone at the bar! They seem interested... 👀")
            time.sleep(3)
            print(Fore.MAGENTA + "Congratulations! You found a partner and are having babies! 🎉👶")
            self.reproduce(current_creature)
        else:
            print(Fore.RED + "You had a drink, but didn't meet anyone interesting... 🍺")
            current_creature.happiness += 5
            current_creature.energy -= 5

        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    def reproduce(self, current_creature):
        if current_creature.age < 18:
            print(Fore.RED + "Your creature is not old enough to go to the bar... They need to grow up first! 🐣")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        if not hasattr(current_creature, 'reproduction_count'):
            current_creature.reproduction_count = 0  # compteur ken
        current_creature.partner = "Someone"
        current_creature.happiness += 20
        current_creature.energy -= 10

        # limit 3
        if current_creature.reproduction_count < 3:
            current_creature.reproduction_count += 1
            print(Fore.YELLOW + f"Baby number {current_creature.reproduction_count} is on the way! 🍼")
            time.sleep(3)
        else:
            print(Fore.YELLOW + "Looks like your creature has decided to start a family. No more babies for now! 🛑")

        if current_creature.reproduction_count > 0:
            print(Fore.CYAN + f"Your creature now has {current_creature.reproduction_count} little ones! Get ready for sleepless nights! 🍼😴")
            time.sleep(3)


