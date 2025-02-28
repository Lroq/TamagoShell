from creature.creature_manager import CreatureManager
from creature.creature_menu import creature_menu
from colorama import Fore, Style, init

init(autoreset=True)


class MainCreatureMenu:
    @staticmethod
    def display_menu():
        print(Fore.BLUE + Style.BRIGHT + "===================================")
        print(Fore.BLUE + Style.BRIGHT + "       MENU PRINCIPAL")
        print(Fore.BLUE + Style.BRIGHT + "===================================")
        print(Fore.BLUE + Style.BRIGHT + "\n1. Créer une nouvelle créature")
        print(Fore.BLUE + Style.BRIGHT + "2. Charger une créature existante")
        print(Fore.BLUE + Style.BRIGHT + "3. Retour au menu principal")
        print(Fore.BLUE + Style.BRIGHT + "===================================")
        choix = input(Fore.GREEN + Style.BRIGHT + "\nQuel est votre choix ?\n")
        print(Fore.BLUE + Style.BRIGHT + "===================================\n")

        if choix == "1":
            creature = creature_menu()
            print(Fore.BLUE + Style.BRIGHT + "\nVoulez-vous sauvegarder cette créature ?")
            save = input(Fore.GREEN + Style.BRIGHT + "Choix 1 pour sauvegarder, 2 pour ne pas sauvegarder\n")

            if save == "1":
                CreatureManager().save_creature(creature)
                print(Fore.GREEN + Style.BRIGHT + "La créature a été sauvegardée avec succès !")
            else:
                print(Fore.RED + Style.BRIGHT + "La créature n'a pas été sauvegardée.")