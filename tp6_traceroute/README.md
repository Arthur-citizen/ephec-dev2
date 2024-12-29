# Traceroute Script

Un script Python simple pour effectuer un traceroute vers une cible spécifiée (URL ou adresse IP). Il offre des options pour un affichage progressif des résultats et la sauvegarde des adresses IP dans un fichier.

## Fonctionnalités

- Exécute un traceroute vers une URL ou une adresse IP.
- Option d'afficher les adresses IP des étapes progressivement dans la console.
- Possibilité de sauvegarder les résultats dans un fichier texte.
- Compatible avec les systèmes d'exploitation Windows, Linux et macOS.

## Prérequis

- Python 3.x doit être installé sur votre système.
- Le programme `traceroute` ou `tracert` doit être disponible :
  - `tracert` pour Windows (installé par défaut).
  - `traceroute` pour Linux/macOS (peut nécessiter une installation via un gestionnaire de paquets).

## Installation

1. Clonez ce dépôt ou téléchargez le fichier script.
2. Assurez-vous que le fichier est nommé correctement, par exemple : `traceroute_script.py`.

## Utilisation

1. **Exécutez le script dans un terminal :**

   ```bash
   python traceroute_script.py

   # Traceroute Script

Un script Python permettant d'effectuer un traceroute vers une cible spécifiée (URL ou adresse IP). Il offre deux modes d'utilisation : interactif ou via des arguments en ligne de commande. Les résultats peuvent être affichés progressivement et/ou sauvegardés dans un fichier.

## Fonctionnalités

- Exécute un traceroute vers une URL ou une adresse IP.
- Deux modes d'utilisation :
  - **Mode interactif :** Saisie guidée des informations par l'utilisateur.
  - **Mode en ligne de commande :** Utilisation d'arguments pour automatiser l'exécution.
- Option d'afficher les résultats progressivement dans la console.
- Possibilité de sauvegarder les résultats dans un fichier texte.
- Compatible avec les systèmes Windows et Linux.

## Prérequis

- **Python 3.x** doit être installé.
- Le programme `traceroute` ou `tracert` doit être disponible sur votre système :
  - `tracert` pour Windows (installé par défaut).
  - `traceroute` pour Linux/macOS (peut nécessiter une installation via un gestionnaire de paquets).

## Installation

1. Clonez ce dépôt ou téléchargez le fichier script.
2. Assurez-vous que le fichier est nommé correctement, par exemple : `traceroute_script.py`.

## Utilisation

### Mode interactif

Exécutez le script sans arguments :

```bash
python traceroute_script.py
```
### Mode en ligne de commande

Exécutez le script sans 

```bash
python traceroute_script.py <target> [-p] [-o <output_file>]
```
1. < target > : Remplacez par l'URL ou l'adresse IP de la cible. (Exemple : www.google.com ou 8.8.8.8)
2. -p : (Optionnel) Affiche les résultats progressivement dans la console.
3. -o <output_file> : (Optionnel) Spécifie le fichier où sauvegarder les résultats (Exemple : resultat.txt).
