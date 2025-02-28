from creature.creature_manager import CreatureManager
from colorama import Fore, Style, init

init(autoreset=True)


class CreatureMenu:
    def __init__(self):
        self.creature_speciess = {
            "1": "😺 Cat",
            "2": "🐶 Dog",
            "3": "💡 Imaginary Creature",
            "4": "🤮 Mutant Slime",
            "5": "🐉 Majestic Dragon",
            "6": "🦊 Cunning Fox",
            "7": "👽 Curious Alien",
            "8": "🕷️ Cybernetic Spider",
            "9": "🤖 Autonomous Robot",
            "10": "🔥 Reborn Phoenix",
            "11": "🦄 Mystic Unicorn",
            "12": "👤 Human",
        }
        self.accessory_options = {
            "1": "🎩 Hat",
            "2": "🕶️ Glasses",
            "3": "🧣 Scarf",
            "4": "🧤 Gloves",
            "5": "🥾 Boots",
            "6": "🎧 Headphones",
            "7": "📿 Necklace",
            "8": "📿 Bracelet",
            "9": "💍 Ring",
            "10": "👂 Earrings",
            "11": "⌚ Watch",
            "12": "⛑️ Helmet",
        }

    def choose_creature(self):
        print(Fore.BLUE + Style.BRIGHT + "\nChoose your creature species:")
        print(
            Fore.BLUE
            + Style.BRIGHT
            + "--------------------------------------------------------"
        )
        for key, value in self.creature_speciess.items():
            print(Fore.YELLOW + Style.BRIGHT + f"{key}. {value}")
        print(
            Fore.BLUE
            + Style.BRIGHT
            + "--------------------------------------------------------"
        )

        choice = input(Fore.GREEN + Style.BRIGHT + "\nWhat is your choice? \n")
        creature = self.creature_speciess.get(choice)

        if creature:
            name = input(Fore.GREEN + Style.BRIGHT + "Give a name to your creature: ")
            print(
                Fore.BLUE
                + Style.BRIGHT
                + f"The chosen species for your creature is a {creature}, named {name}"
            )
            return {"species": creature, "name": name}
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice, please try again.")
            return self.choose_creature()

    def add_accessory(self):
        accessories = []
        while True:
            print(
                Fore.BLUE
                + Style.BRIGHT
                + "\nChoose an accessory to add to your creature:"
            )
            print(
                Fore.BLUE
                + Style.BRIGHT
                + "--------------------------------------------------------"
            )
            for key, value in self.accessory_options.items():
                print(Fore.YELLOW + Style.BRIGHT + f"{key}. {value}")
            print(Fore.YELLOW + Style.BRIGHT + "12. Finish")
            print(
                Fore.BLUE
                + Style.BRIGHT
                + "--------------------------------------------------------"
            )

            if accessories:
                print(
                    Fore.BLUE + Style.BRIGHT + "Your current selection:",
                    ", ".join(accessories),
                )

            choice = input(Fore.GREEN + Style.BRIGHT + "\nWhat is your choice?\n")

            if choice == "12":
                break

            item = self.accessory_options.get(choice)
            if item:
                accessories.append(item)
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid choice, please try again.")

        return accessories


def creature_menu():
    menu = CreatureMenu()
    creature = menu.choose_creature()
    accessories = menu.add_accessory()
    creature["accessories"] = accessories

    creature["health"] = 100
    creature["hunger"] = 100
    creature["age"] = 1
    creature["is_alive"] = True

    print(
        Fore.BLUE
        + Style.BRIGHT
        + "\n---------------------YOUR CREATURE---------------------"
    )
    print(
        Fore.BLUE
        + Style.BRIGHT
        + f"Your {creature['species']} named {creature['name']} has the following accessories: {', '.join(accessories) if accessories else 'None'}."
    )
    print(
        Fore.BLUE
        + Style.BRIGHT
        + "--------------------------------------------------------"
    )

    return creature
