import threading
import time
import random
import os
from creature.creature import Creature
from creature.creature_manager import CreatureManager
from game.actions.actions import Actions
from colorama import Fore, init, Style
from datetime import datetime, timedelta

current_creature = None
init(autoreset=True)
current_time = datetime.now()

def update_time():
    global current_time
    while True:
        time.sleep(1)  # 1 second IRL
        current_time += timedelta(minutes=10)  # 10 minutes in-game

def decrease_stats():
    global current_creature
    while current_creature and current_creature.is_alive:
        time.sleep(10)

        current_creature.hunger = max(0, current_creature.hunger - 5)
        current_creature.energy = max(0, current_creature.energy - 2)
        current_creature.health = max(0, current_creature.health - 5)

        if current_creature.health <= 5 and current_creature.health > 0:
            print(Fore.RED + "\n⚠️ WARNING: Your creature is critically low on health! ⚠️")

        if current_creature.health <= 0:
            print(Fore.RED + "\n💀 Game Over! Your creature has died... 💀")
            print(Fore.RED + "Better luck next time! 🥀")
            current_creature.is_alive = False
            time.sleep(2)
            exit()

def display_ui():
    os.system('cls' if os.name == 'nt' else 'clear')
    current_creature.display()

    print(f"{Fore.YELLOW}Today is {current_time.strftime('%Y-%m-%d')} and the time is {current_time.strftime('%H:%M')}\n")
    print(Fore.BLUE + "What would you like to do with your creature:")
    print(Fore.BLUE + Style.BRIGHT + "1. Eat")
    print(Fore.BLUE + Style.BRIGHT + "2. Sleep")
    print(Fore.BLUE + Style.BRIGHT + "3. Play")
    print(Fore.BLUE + Style.BRIGHT + "4. Heal")
    print(Fore.BLUE + Style.BRIGHT + "5. Go to the bar")

def game():
    global current_creature
    manager = CreatureManager()
    creature_data = manager.load_creatures()

    if creature_data:
        try:
            creature_data.pop('type', None)
            current_creature = Creature(**creature_data)
            threading.Thread(target=decrease_stats, daemon=True).start()
            game_loop()
        except TypeError as e:
            print(f"Error while creating the creature: {e}")
    else:
        return

def game_loop():
    global current_creature, current_time
    while current_creature.is_alive:
        display_ui()

        choice = input("\nWhat activity would you like to do?\n")

        match choice:
            case "1":
                Actions().eat(current_creature)
                current_time += timedelta(minutes=30)
            case "2":
                sleep_time = Actions().sleep(current_creature)
                current_time += timedelta(hours=8)
            case "3":
                Actions().play(current_creature)
                current_time += timedelta(hours=1)
            case "4":
                Actions().update_health(current_creature)
                current_time += timedelta(hours=random.randint(1, 24))
            case "5":
                Actions().go_to_bar(current_creature)
                current_time += timedelta(hours=random.random.randit(1, 6))
            case _:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                continue

        time.sleep(1)
        display_ui()
