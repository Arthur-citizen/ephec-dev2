import csv
import os
from typing import List
import sys

def calculate_average(numbers: List[float]) -> float:
    """
    Calcul la moyenne d'une liste de nombres.

    Args:
        numbers (List[float]): Une list de valeurs numériques.

    Returns:
        float: La moyenne des nombres dans la liste.
               Retourne 0.0 si la liste est vide.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def consolidate_csv_files(directory: str, output_file: str) -> None:
    """
    Consolide plusieurs fichier CSV dans un dossier en un fichier unique.

    Args:
        directory (str): Chemin vers le dossier contenant les fichiers CSV.
        output_file (str): Chemin depuis le script pour créer le dossier consolidé.
    """
    consolidated_data = []
    headers = None

    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                file_headers = next(reader)

                if headers is None:
                    headers = file_headers
                    consolidated_data.append(headers)
                elif headers != file_headers:
                    raise ValueError(f"Inconsistent headers in file: {file_name}")

                for row in reader:
                    consolidated_data.append(row)

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(consolidated_data)


def generate_summary_report(csv_file: str, report_file: str) -> None:
    """
    Génère un rapport récapitulatif avec la moyenne des prix par catégorie.

    Args:
        csv_file (str): Chemin du fichier CSV d'entrée.
        report_file (str): Chemin du fichier CSV de sortie pour le rapport.

    Returns:
        None
    """
    # Dictionnaire pour stocker les totaux par catégorie
    category_data = {}

    # Lecture du fichier CSV d'entrée
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Lecture des données avec les noms exacts des colonnes
            categorie = row.get("catégorie", "Inconnue")
            prix_unitaire = float(row.get("prix", 0.0))
            quantite = int(row.get("quantite", 0))

            # Initialisation de la catégorie si nécessaire
            if categorie not in category_data:
                category_data[categorie] = {"total_prix": 0.0, "total_quantite": 0}

            # Mise à jour des totaux
            category_data[categorie]["total_prix"] += prix_unitaire * quantite
            category_data[categorie]["total_quantite"] += quantite

    # Écriture du fichier de rapport
    with open(report_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["catégorie", "prix_moyen", "quantité_en_stock"])

        # Calcul de la moyenne par catégorie et écriture dans le fichier
        for categorie, data in category_data.items():
            total_prix = data["total_prix"]
            total_quantite = data["total_quantite"]
            prix_moyen = total_prix / total_quantite if total_quantite > 0 else 0.0
            writer.writerow([categorie, round(prix_moyen, 2), total_quantite])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python stock_manager.py <command> [args...]")
        print("Commands:")
        print("  consolidate <input_directory> <output_file>")
        print("  summarize <input_file> <report_file>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "consolidate":
        if len(sys.argv) != 4:
            print("Usage: python stock_manager.py consolidate <input_directory> <output_file>")
            sys.exit(1)
        input_directory = sys.argv[2]
        output_file = sys.argv[3]
        consolidate_csv_files(input_directory, output_file)
        print(f"Consolidated files into {output_file}")

    elif command == "summarize":
        if len(sys.argv) != 4:
            print("Usage: python stock_manager.py summarize <input_file> <report_file>")
            sys.exit(1)
        input_file = sys.argv[2]
        report_file = sys.argv[3]
        generate_summary_report(input_file, report_file)
        print(f"Summary report generated: {report_file}")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)