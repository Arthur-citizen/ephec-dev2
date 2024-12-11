# Gestion des Stocks et Rapports Récapitulatifs

Ce programme permet de consolider des fichiers CSV contenant des informations sur les stocks (nom du produit, quantité, prix unitaire, catégorie) et de générer un rapport récapitulatif exportable. Le rapport inclut la moyenne des prix par catégorie.

## Prérequis

- Python 3.7 ou une version ultérieure.
- Le module `sys`, `os`, `typing` et `csv`

## Installation

1. **Clonez le dépôt ou téléchargez les fichiers :**
   ```bash
   git clone <url_du_dépôt>
   cd <nom_du_dépôt>
   ```

2. **Structure des fichiers CSV** :
   Les fichiers CSV doivent contenir les colonnes suivantes :
   - `nom_du_produit` : Nom du produit.
   - `quantite` : Quantité du produit.
   - `prix` : Prix unitaire.
   - `catégorie` : Catégorie du produit.

   Exemple de fichier CSV :
   ```csv
   nom_du_produit,quantite,prix,catégorie
   Stylo,50,1.20,Papeterie
   Cahier,30,2.50,Papeterie
   Clé USB,15,10.00,Électronique
   Souris,25,12.50,Électronique
   ```

## Utilisation

### 1. Consolider plusieurs fichiers CSV en un seul
 
Exécutez la commande suivante dans un terminal depuis le dossier scritp :
```bash
python stock_manager.py consolidate dossier_csv fichier_consolide.csv
```
- `stock_manager.py` : Le nom du script
- `dossier_csv` : Chemin vers le dossier contenant les fichiers CSV à consolider.
- `fichier_consolide.csv` : Nom du fichier CSV consolidé.

### 2. Générer un rapport récapitulatif

Exécutez la commande suivante :
```bash
python stock_manager.py summarize fichier_consolide.csv rapport.csv
```
- `stock_manager.py` : Le nom du script
- `fichier_consolide.csv` : Fichier consolidé généré lors de l'étape précédente.
- `rapport.csv` : Nom du fichier CSV récapitulatif contenant les moyennes par catégorie.

### 3. Exemple complet
1. Placez plusieurs fichiers CSV (par ex. `produits1.csv`, `produits2.csv`) dans un dossier nommé `data/`.
2. Consolidez-les :
   ```bash
   python script.py consolider --input data --output consolidé.csv
   ```
3. Générez le rapport :
   ```bash
   python script.py rapport --input consolidé.csv --output rapport.csv
   ```
4. Consultez le fichier `rapport.csv` pour voir les moyennes par catégorie.

## Fonctionnalités

1. **Consolidation** : Combine plusieurs fichiers CSV contenant les stocks par catégorie ou département.
2. **Rapport de synthèse** : Calcul automatique de la moyenne des prix par catégorie.
3. **Structure simple** : Fonctionne avec des fichiers CSV standard et ne nécessite pas de base de données.

## Personnalisation
Si vos fichiers CSV ont des noms de colonnes différents, vous pouvez modifier les noms directement dans le code Python pour correspondre à vos besoins.
