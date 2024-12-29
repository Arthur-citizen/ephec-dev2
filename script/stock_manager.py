import csv
import os
import sys
from typing import List


def consolidate_csv_files(directory: str, output_file: str) -> None:
    """
    PRE :   - le dossier contient des fichiers CSV à consolider.
            - le nom du dossier ne contient pas de caractères spéciaux ou accentués.
            - le dossier contient au moins un fichier CSV.
    POST :  - Consolide tous les fichiers CSV dans un seul dans le dossier spécifié. 
    RAISES: - ValueError si les en-têtes des fichiers CSV ne sont pas identiques.
            - Exception si aucun fichier CSV n'est trouvé dans le dossier.
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
        else:
            raise Exception("aucun fichier CSV trouvé dans le dossier")

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(consolidated_data)


def generate_summary_report(csv_file: str, report_file: str) -> None:
    """
    PRE :   - Les fichiers CSV on les colonnes "catégorie"(str), "prix"(float) et "quantité"(int).
    POST :  - Crée un fichier CSV à l'emplacement `report_file` avec les colonnes : "catégorie", "prix_moyen", "quantité_en_stock".
            - Les valeurs de "prix_moyen" et "quantité_en_stock" sont calculées pour chaque catégorie présente dans le fichier CSV spécifié.
    RAISES: - ValueError si les données ne sont pas convertibles en float ou int.
            - KeyError si une colonne manque dans le fichier CSV.
    """
    # Dictionnaire pour stocker les totaux par catégorie
    category_data = {}
    # Lecture du fichier CSV d'entrée
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Lecture des données avec les noms exacts des colonnes
            categorie = row.get("catégorie", "Inconnue")
            try:
                prix_unitaire = float(row["prix"])
                quantite = int(row["quantite"])
            except (ValueError, KeyError):
                # print(f"Ligne ignorée à cause de données invalides: {row}")
                continue  # Ignorer cette ligne et passer à la suivante

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
        print("  interact")
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

    elif command == "interact":
        print("=== Mode interactif ===")
        action = input("Quelle action souhaitez-vous effectuer ? (consolidate/summarize): ").strip().lower()

        if action == "consolidate":
            input_directory = input("Entrez le chemin du dossier contenant les fichiers CSV à consolider: ").strip()
            output_file = input("Entrez le nom du fichier de sortie pour les données consolidées: ").strip()
            try:
                consolidate_csv_files(input_directory, output_file)
                print(f"Les fichiers CSV ont été consolidés dans {output_file}.")
            except Exception as e:
                print(f"Erreur lors de la consolidation : {e}")

        elif action == "summarize":
            input_file = input("Entrez le chemin du fichier CSV à résumer: ").strip()
            report_file = input("Entrez le nom du fichier de sortie pour le rapport: ").strip()
            try:
                generate_summary_report(input_file, report_file)
                print(f"Le rapport a été généré dans {report_file}.")
            except Exception as e:
                print(f"Erreur lors de la génération du rapport : {e}")

        else:
            print("Action non reconnue. Veuillez utiliser 'consolidate' ou 'summarize'.")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
