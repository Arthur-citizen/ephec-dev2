#Utilisation de chatGPT mais coed compris
# Classe Fichier_joint
class Fichier_joint:
    def __init__(self, nom, taille, path):
        self.nom = nom
        self.taille = taille
        self.path = path

# Classe Email
class Email:
    def __init__(self, expediteur, destination, titre="", texte=""):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []

    def ajouter_fichier_joint(self, fichier):
        self.fichiers_joints.append(fichier)

# Exemple d'utilisation
email = Email("alice@example.com", "bob@example.com", "Projet", "Bonjour, voici le projet.")
email.ajouter_fichier_joint(Fichier_joint("document.pdf", 1024, "document/"))

print(f"De: {email.expediteur}, À: {email.destination}")
print(f"Titre: {email.titre}, Texte: {email.texte}")
print("Fichiers joints:")
for f in email.fichiers_joints:
    print(f"  - {f.nom}, {f.taille} octets")