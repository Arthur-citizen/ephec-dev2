import subprocess
import re
import platform

def traceroute(target, progressive, output_file):
    command = ["traceroute", target] if platform.system() != "Windows" else ["tracert", target]

    try:
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            f = open(output_file, "w") if output_file else None  # Ouvrir le fichier si nécessaire
            try:
                for line in proc.stdout:
                    ip = extract_ip(line)
                    if ip:
                        if progressive:
                            print(ip)
                        if f:
                            f.write(ip + "\n")
            finally:
                if f:
                    f.close()
            proc.wait()
    except FileNotFoundError:
        print("Erreur : La commande 'traceroute' ou 'tracert' n'est pas disponible sur ce système.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

def extract_ip(line):
    match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
    return match.group(0) if match else None

if __name__ == "__main__":
    # demande l'URL ou l'adresse IP de la cible
    target = input("Entrez l'URL ou l'adresse IP de la cible : ").strip()
    # Demande si l'affichage progressif doit être activé 
    progressive = input("Souhaitez-vous un affichage progressif des résultats ? (y/n) : ").strip().lower() == "y"
    # Demande si un rapport doit être généré 
    save_report = input("Souhaitez-vous générer un rapport ? (y/n) : ").strip().lower() == "y"
    output_file = None
    if save_report:
        output_file = input("Entrez le nom du fichier pour enregistrer les résultats (.txt) : ").strip()

    traceroute(target, progressive, output_file)
