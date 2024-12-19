#Utilisation de chatGPT, code compris et modifié
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
    
    def __str__(self):
        return f"Animal de regime {self.regime} et habitat {self.habitat}. Tête : {self.tete.description}, Corp : {self.corp.description}, Membres : {', '.join([membre.nom for membre in self.membres])}"


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

class Tigre(Animal):
    def __init__(self, habitat):
        super().__init__(regime="Carnivore", habitat=habitat)

# Exemple d'utilisation
if __name__ == "__main__":

    # Création d'un Lapin
    lapin = Lapin(habitat=Habitat("Prairie"))
    lapin.ajouter_membre(Membre("Patte avant gauche"))
    lapin.ajouter_membre(Membre("Patte avant droite"))
    lapin.ajouter_membre(Membre("Patte arrière gauche"))
    lapin.ajouter_membre(Membre("Patte arrière droite"))

    # Affichage des informations du lapin
    print("Informations sur le Lapin :")
    print(lapin)

    # Création d'un tigre
    tigre = Tigre(habitat=Habitat("Foret"))
    tigre.ajouter_membre(Membre("Patte 1"))
    tigre.ajouter_membre(Membre("Patte 2"))
    tigre.ajouter_membre(Membre("Patte 3"))
    tigre.ajouter_membre(Membre("Patte 4"))

    print("\nInformations sur le tigre :")
    print(tigre)