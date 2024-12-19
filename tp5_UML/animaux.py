#Utilisation de chatGPT et code compris
# Classe Animal
class Animal:
    def __init__(self, regime, habitat):
        self.regime = regime  # Herbivore ou Carnivore
        self.habitat = habitat  # L'habitat de l'animal
        self.tete = Tete()
        self.corp = Corp()
        self.membres = []  # Liste des membres

    def ajouter_membre(self, membre):
        self.membres.append(membre)


# Classe Tete
class Tete:
    def __init__(self):
        self.description = "Tête d'animal"

# Classe Corp
class Corp:
    def __init__(self):
        self.description = "Corps d'animal"

# Classe Membre
class Membre:
    def __init__(self, nom):
        self.nom = nom

# Classe Habitat
class Habitat:
    def __init__(self, nom):
        self.nom = nom

# Classes (héritage)
class Lapin(Animal):
    def __init__(self, habitat):
        super().__init__(regime="Herbivore", habitat=habitat)

class Mouton(Animal):
    def __init__(self, habitat):
        super().__init__(regime="Herbivore", habitat=habitat)

# Exemple d'utilisation
if __name__ == "__main__":
    prairie = Habitat("Prairie")

    # Création d'un Lapin
    lapin = Lapin(habitat=prairie)
    lapin.ajouter_membre(Membre("Patte avant gauche"))
    lapin.ajouter_membre(Membre("Patte avant droite"))
    lapin.ajouter_membre(Membre("Patte arrière gauche"))
    lapin.ajouter_membre(Membre("Patte arrière droite"))

    # Affichage des informations du lapin
    print("Informations sur le Lapin :")
    lapin.afficher_info()

    # Création d'un Mouton
    mouton = Mouton(habitat=prairie)
    mouton.ajouter_membre(Membre("Patte 1"))
    mouton.ajouter_membre(Membre("Patte 2"))
    mouton.ajouter_membre(Membre("Patte 3"))
    mouton.ajouter_membre(Membre("Patte 4"))

    print("\nInformations sur le Mouton :")
    mouton.afficher_info()