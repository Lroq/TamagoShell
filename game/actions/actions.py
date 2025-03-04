import os
import time
import random
from colorama import Fore, init
from datetime import timedelta
from creature.creature import Creature

init(autoreset=True)

class Actions:
    def __init__(self):
        self.food = {
            "1": "🍔 Hamburger",
            "2": "🍕 Pizza",
            "3": "🍣 Sushi",
            "4": "🍝 Pasta",
        }

    def check_limits(self, value, max_value=100, min_value=5):
        if value > max_value:
            value = max_value
        elif value < min_value:
            print(Fore.RED + f"ALERT: Your creature's attribute is critically low! (Value: {value})")
        return value

    def eat(self, current_creature):
        print(Fore.BLUE + "\nChoose the food for your creature:")
        print(Fore.CYAN + "╔════════════════════════════════════════╗")
        print(Fore.CYAN + "║         Available Foods:               ║")
        print(Fore.CYAN + "╠════════════════════════════════════════╣")
        for key, value in self.food.items():
            print(f"║     {key}. {value}                        ║")
        print(Fore.CYAN + "╚════════════════════════════════════════╝")
        print()

        choice = input(Fore.GREEN + "What is your choice? \n")
        food = self.food.get(choice)

        if food:
            print(Fore.BLUE + f"\nThe chosen food is {food}, it's a delight! 🍽️\n")
            print(f"Before: Hunger: {current_creature.hunger}, Health: {current_creature.health}")
            current_creature.hunger += 10
            current_creature.hunger = self.check_limits(current_creature.hunger)
            current_creature.health += 10
            current_creature.health = self.check_limits(current_creature.health)

            time.sleep(3)
            print(f"After: Hunger: {current_creature.hunger}, Health: {current_creature.health}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return food
        else:
            print(Fore.RED + "Invalid choice, please try again.")
            return self.eat(current_creature)

    def sleep(self, current_creature):
        print(Fore.BLUE + "\nYour creature is now sleeping... 💤")
        print(f"Before: Health: {current_creature.health}, Energy: {current_creature.energy}, Hungry: {current_creature.hunger}")
        current_creature.energy += 10
        current_creature.energy = self.check_limits(current_creature.energy)
        current_creature.health += 10
        current_creature.health = self.check_limits(current_creature.health)
        current_creature.hunger -= 10
        current_creature.hunger = self.check_limits(current_creature.hunger)

        time.sleep(3)
        print(f"After: Health: {current_creature.health}, Energy: {current_creature.energy}, Hungry: {current_creature.hunger}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        if not hasattr(current_creature, 'sleep_count'):
            current_creature.sleep_count = 0
        current_creature.sleep_count += 1

        if current_creature.sleep_count % 4 == 0:
            current_creature.age_up()

    def play(self, current_creature):
        print(Fore.BLUE + "\nYour creature is now playing. 🎮")
        print("╔════════════════════════════════════════╗")
        print("║        Playing... Getting excited!     ║")
        print("╚════════════════════════════════════════╝")
        print(f"Before: Happiness: {current_creature.happiness}, Energy: {current_creature.energy}, Health: {current_creature.health}")
        current_creature.happiness += 10
        current_creature.happiness = self.check_limits(current_creature.happiness)
        current_creature.energy -= 5
        current_creature.energy = self.check_limits(current_creature.energy)
        current_creature.health -= 12
        current_creature.health = self.check_limits(current_creature.health)

        time.sleep(3)

        new_creature = Creature(name="DefaultName", species="DefaultSpecies", accessories="DefaultAccessories")
        if random.randint(1, 5) == 1:  # 1/5 chance
            new_creature.random_event()
            print(Fore.MAGENTA + "I found something exciting! Wuwu! 🎉")
        else:
            print(Fore.RED + "Nothing found, just chilling... 😌")

        print(f"After: Happiness: {current_creature.happiness}, Energy: {current_creature.energy}, Health: {current_creature.health}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    def update_health(self, current_creature):
        if current_creature.health < 100:
            current_creature.health += 10
            current_creature.health = self.check_limits(current_creature.health)

            print(Fore.GREEN + f"Your creature is healed! Current health: {current_creature.health}/100\n")
        elif current_creature.health == 100:
            print(Fore.BLUE + "Your creature's health is already at full capacity!\n")

        if current_creature.health == 5:
            print(Fore.RED + "ALERT: Your creature is exhausted! It needs rest or food.")

    def go_to_bar(self, current_creature):
        if current_creature.age < 18:
            print(Fore.RED + "\nYour creature is not old enough to go to the bar... They need to grow up first! 🐣")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        print(Fore.BLUE + "\nYour creature is heading to the bar... 🍻")

        if random.randint(1, 5) == 1:
            print(Fore.GREEN + "You met someone at the bar! They seem interested... 👀")
            time.sleep(3)
            print(Fore.MAGENTA + "Congratulations! You found a partner and are having babies! 🎉👶")
            self.reproduce(current_creature)
        else:
            print(Fore.RED + "You had a drink, but didn't meet anyone interesting... 🍺")
            print(f"Before: Happiness: {current_creature.happiness}, Energy: {current_creature.energy}")
            current_creature.happiness += 5
            current_creature.happiness = self.check_limits(current_creature.happiness)
            current_creature.energy -= 5
            current_creature.energy = self.check_limits(current_creature.energy)

            time.sleep(3)
            print(f"After: Happiness: {current_creature.happiness}, Energy: {current_creature.energy}")
        time.sleep(3)

        new_creature = Creature(name="DefaultName", species="DefaultSpecies", accessories="DefaultAccessories")
        if new_creature.random_event():
            print(Fore.YELLOW + "I found something exciting! Wuwu! 🎉")
            time.sleep(2)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    def reproduce(self, current_creature):
        if current_creature.age < 18:
            print(Fore.RED + "\nYour creature is not old enough to reproduce... They need to grow up first! 🐣")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        if not hasattr(current_creature, 'reproduction_count'):
            current_creature.reproduction_count = 0  # reproduction counter

        current_creature.partner = "Someone"
        current_creature.happiness += 20
        current_creature.happiness = self.check_limits(current_creature.happiness)
        current_creature.energy -= 10
        current_creature.energy = self.check_limits(current_creature.energy)

        time.sleep(3)
        print(f"After: Happiness: {current_creature.happiness}, Energy: {current_creature.energy}")

        # limit 3 babies
        if current_creature.reproduction_count < 3:
            current_creature.reproduction_count += 1
            print(Fore.YELLOW + f"Baby number {current_creature.reproduction_count} is on the way! 🍼")
            time.sleep(3)
        else:
            print(Fore.RED + "No more babies for now! Your creature has decided to start a family. 🛑")

        if current_creature.reproduction_count > 0:
            print(Fore.MAGENTA + f"Your creature now has {current_creature.reproduction_count} little ones! Get ready for sleepless nights! 🍼😴")
            time.sleep(3)
