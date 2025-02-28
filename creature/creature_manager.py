import json
import os
from colorama import Fore, init

init(autoreset=True)

SAVE_FILE = "creature.json"


class CreatureManager:
    def __init__(self, save_file=SAVE_FILE):
        self.save_file = save_file

    def save_creature(self, creature):
        try:
            if os.path.exists(self.save_file):
                with open(self.save_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
            else:
                data = []

            # if missing keys in the dictionary
            creature.setdefault("health", 100)
            creature.setdefault("is_alive", True)
            creature.setdefault("hunger", 100)
            creature.setdefault("age", 1)
            creature.setdefault("energy", 100)
            creature.setdefault("happiness", 100)
            creature.setdefault("sanity", 100)

            data.append(creature)

            with open(self.save_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            print(Fore.GREEN + "\n✅ Creature successfully saved!")
        except Exception as e:
            print(Fore.RED + f"❌ Error while saving: {e}")

    def load_creatures(self):
        if not os.path.exists(self.save_file):
            print(Fore.YELLOW + "\n⚠️ No save file found.")
            return None

        try:
            with open(self.save_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not data:
                print(Fore.YELLOW + "\n⚠️ No saved creatures found.")
                return None

            print(Fore.BLUE + "\n📜 List of saved creatures:")
            for index, creature in enumerate(data, 1):
                name = creature.get("name", "Unknown")
                creature_species = creature.get("species", "Unknown")
                health = creature.get("health", 100)
                hunger = creature.get("hunger", 100)
                age = creature.get("age", 1)
                energy = creature.get("energy", 100)
                happiness = creature.get("happiness", 100)
                sanity = creature.get("sanity", 100)

                is_alive = creature.get("is_alive", True)
                print(
                    Fore.BLUE
                    + f"{index}. 🛡️  Name: {name} | ⚡ species: {creature_species} | ❤️  Health: {health} | 🍔 Hunger: {hunger} | 🕒 Age: {age} | 🧬 Alive: {is_alive} | 🔋 Energy: {energy} | 😊 Happiness: {happiness} | 🏥 Sanity: {sanity}"
                )
            while True:
                try:
                    choice = int(
                        input(
                            Fore.GREEN
                            + "\n➡️  Enter the number of the creature to select: "
                        )
                    )
                    if 1 <= choice <= len(data):
                        print(Fore.GREEN + "\n✅ Creature successfully loaded!")
                        return data[choice - 1]
                    else:
                        print(Fore.RED + "\n❌ Invalid number. Please try again.")
                except ValueError:
                    print(
                        Fore.RED
                        + "\n❌ Invalid input. Please enter a number from the list."
                    )

        except Exception as e:
            print(Fore.RED + f"❌ Error while loading saves: {e}")
            return None
