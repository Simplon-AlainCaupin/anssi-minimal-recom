#!/usr/bin/python3
import os

def split_file(input_file):
    if not os.path.exists(input_file): # Vérifie l'existence du fichier en entrée
        print(f"Input file '{input_file}' not found.")
        return

    with open(input_file, 'r') as f:
        lines = f.readlines()

    # output_dir = "output"
    # os.makedirs(output_dir, exist_ok=True)

    task_number = 1
    current_output_file = None

    for line in lines: # Boucle pour incrémenter le nom du ficher de 01 à "n" (nb de lignes vides)
        if line.strip():  # Vérifie si la ligne est vide ou non
            if current_output_file is None:
            #  current_output_file = open(f"{output_dir}/{task_number:02d}-task", "w")
               current_output_file = open(f"./{task_number:02d}-task.yml", "w")
            current_output_file.write(line)
        else:
            if current_output_file is not None:
                current_output_file.close()
                task_number += 1
                current_output_file = None

    # Ferme le dernier fichier ouvert par le script
    if current_output_file is not None:
        current_output_file.close()

if __name__ == "__main__":
    input_file = "./tasks.yml"  # chemin vers le ficher "tasks", à changer suivant le nom du fichier
    split_file(input_file)
