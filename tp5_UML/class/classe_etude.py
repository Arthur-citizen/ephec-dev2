# #Utilisation de chatGPT mais code compris et modifié
# Classe Coordonnees
class Coordonnees:
    def __init__(self, adresse: str, telephone: str):
        self.adresse = adresse
        self.telephone = telephone

    def __str__(self):
        return f"Adresse: {self.adresse}, Téléphone: {self.telephone}"

# Classe Personne
class Personne:
    def __init__(self, etatCivil: str, coordonnees: Coordonnees):
        self.etatCivil = etatCivil
        self.coordonnees = coordonnees
    
    def __str__(self):
        return f"État civil: {self.etatCivil}, Coordonnées: {self.coordonnees}"

# Classe Élève
class Eleve(Personne):
    def __init__(self, etatCivil: str, coordonnees: Coordonnees):
        super().__init__(etatCivil, coordonnees)
        self.classe = None  # Référence bidirectionnelle

# Classe Professeur
class Professeur(Personne):
    def __init__(self, etatCivil: str, coordonnees: Coordonnees):
        super().__init__(etatCivil, coordonnees)

# Classe Classe
class Classe:
    def __init__(self, professeur: Professeur):
        if not isinstance(professeur, Professeur):
            raise ValueError("Un professeur valide est requis.")
        self.professeur = professeur
        self.eleves = []

    def __str__(self):
        return f"Professeur: {self.professeur.etatCivil}, Élèves: {', '.join([eleve.etatCivil for eleve in self.eleves])}"
    
    def ajouter_professeur(self, professeur: Professeur):
        self.professeur = professeur

    def ajouter_eleve(self, eleve: Eleve):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
            eleve.classe = self
        else:
            print("La classe est complète (30 élèves maximum).")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création des coordonnées
    coord_prof = Coordonnees("123 Rue des Professeurs", "0123456789")
    coord_eleve1 = Coordonnees("456 Rue des Élèves", "0987654321")
    coord_eleve2 = Coordonnees("789 Rue des Étudiants", "0678943210")

    # Création des personnes
    professeur = Professeur("Mr. Dupont", coord_prof)
    eleve1 = Eleve("Jean Martin", coord_eleve1)
    eleve2 = Eleve("Marie Durand", coord_eleve2)

    # Création d'une classe
    ma_classe = Classe(professeur)

    # Ajout d'élèves
    ma_classe.ajouter_eleve(eleve1)
    ma_classe.ajouter_eleve(eleve2)

    # Affichage des informations de la classe
    print("Informations de la Classe :")
    print(ma_classe)