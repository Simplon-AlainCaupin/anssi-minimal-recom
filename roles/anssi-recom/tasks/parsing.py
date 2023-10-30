#!/usr/bin/python3
import requests
import os

# Récupération du playbook sur le repo officiel rhel8 
url = 'https://raw.githubusercontent.com/RedHatOfficial/ansible-role-rhel8-anssi_bp28_minimal/b6bfa736d64c6c03105ca421b7959e45d6046f1d/tasks/main.yml'
response = requests.get(url)
playbook_content = response.text

# Séparation des tasks suivant le pattern "- name:"
tasks = playbook_content.split("\n- name: ")[1:]

# Optionnel : remplacer la valeur de output_dir pour changer le répertoire cible 
# par défaut répertoire actuel
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Fichiers générés par une boucle pour chaque itération de "tasks"
for index, task in enumerate(tasks):
    task_content = f"- name: {task.strip()}"
    with open(os.path.join(output_dir, f'task_{index:03d}.yml'), 'w') as task_file:
        task_file.write(task_content)

print("Fichiers générés avec succès dans 'output_dir'")

