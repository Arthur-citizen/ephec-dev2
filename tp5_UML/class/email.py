#Utilisat<ion de chatGPT mais code compris et modifié
import re

# Classe Fichier_joint
class Fichier_joint:
    def __init__(self, nom, taille, path):
        if taille < 0:
            raise ValueError("La taille du fichier ne peut pas être négative.")
        self.nom = nom
        self.taille = taille
        self.path = path

    def __str__(self):
        return f"Fichier: {self.nom}, Taille: {self.taille} octets, Chemin: {self.path}"

# Classe Email
class Email:
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def __init__(self, expediteur, destination, titre="", texte=""):
        if not re.match(self.EMAIL_REGEX, expediteur):
            raise ValueError(f"Adresse email invalide: {expediteur}")
        if not re.match(self.EMAIL_REGEX, destination):
            raise ValueError(f"Adresse email invalide: {destination}")

        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []

    def ajouter_fichier_joint(self, fichier):
        if not isinstance(fichier, Fichier_joint):
            raise TypeError("L'objet ajouté doit être une instance de Fichier_joint.")
        self.fichiers_joints.append(fichier)

    def __str__(self):
        fichiers = "\n".join([str(fichier) for fichier in self.fichiers_joints])
        return f"De: {self.expediteur}, À: {self.destination}\nTitre: {self.titre}\nTexte: {self.texte}\nFichiers joints:\n{fichiers}"

# Exemple d'utilisation
if __name__ == "__main__":
    email = Email("alice@example.com", "bob@example.com", "Projet", "Bonjour, voici le projet.")
    email.ajouter_fichier_joint(Fichier_joint("document.pdf", 1024, "document/"))

    print(email)