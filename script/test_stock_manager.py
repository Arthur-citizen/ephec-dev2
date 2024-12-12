import unittest
import csv
import os
from io import StringIO
from stock_manager import generate_summary_report  # Remplacez par le nom du fichier contenant votre code

class TestGenerateSummaryReport(unittest.TestCase):

    def setUp(self):
        # Configuration des fichiers temporaires
        self.input_csv = "test_input.csv"
        self.output_csv = "test_output.csv"

    def tearDown(self):
        # Nettoyage des fichiers temporaires
        if os.path.exists(self.input_csv):
            os.remove(self.input_csv)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)

    def write_csv(self, filename, content):
        """Helper pour écrire un fichier CSV."""
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(content)

    def read_csv(self, filename):
        """Helper pour lire un fichier CSV."""
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            return list(reader)

    def test_generate_summary_report_basic(self):
        # Données d'entrée
        input_data = [
            ["catégorie", "prix", "quantite"],
            ["Fruits", "2.5", "10"],
            ["Légumes", "1.2", "5"],
            ["Fruits", "3", "5"]
        ]
        
        # Fichier attendu
        expected_output = [
            ["catégorie", "prix_moyen", "quantité_en_stock"],
            ["Fruits", "2.67", "15"],
            ["Légumes", "1.2", "5"]
        ]

        self.write_csv(self.input_csv, input_data)

        # Appel de la fonction
        generate_summary_report(self.input_csv, self.output_csv)

        # Vérification du fichier de sortie
        output_data = self.read_csv(self.output_csv)
        self.assertEqual(output_data, expected_output)

    def test_generate_summary_report_empty(self):
        # Données d'entrée vides
        input_data = [["catégorie", "prix", "quantite"]]

        # Fichier attendu
        expected_output = [["catégorie", "prix_moyen", "quantité_en_stock"]]

        self.write_csv(self.input_csv, input_data)

        # Appel de la fonction
        generate_summary_report(self.input_csv, self.output_csv)

        # Vérification du fichier de sortie
        output_data = self.read_csv(self.output_csv)
        self.assertEqual(output_data, expected_output)

    def test_generate_summary_report_invalid_data(self):
        # Données d'entrée avec des valeurs invalides
        input_data = [
            ["catégorie", "prix", "quantite"],
            ["Fruits", "abc", "10"],
            ["Légumes", "1.2", "xyz"]
        ]

        # Fichier attendu
        expected_output = [["catégorie", "prix_moyen", "quantité_en_stock"]]

        self.write_csv(self.input_csv, input_data)

        # Appel de la fonction
        generate_summary_report(self.input_csv, self.output_csv)

        # Vérification du fichier de sortie
        output_data = self.read_csv(self.output_csv)
        self.assertEqual(output_data, expected_output)

if __name__ == "__main__":
    unittest.main()
