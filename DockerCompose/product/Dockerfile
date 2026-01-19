# Image de base officielle Python 3.10
FROM python:3.10

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie le fichier des dépendances dans le conteneur
COPY requirement.txt /app/requirement.txt

# Installation des dépendances Python
RUN pip install -r requirement.txt

# On copie tout le reste des fichiers de l'appli dans /app
COPY . /app

# Commande lancée au démarrage du conteneur
# -> exécute l'API Flask
CMD ["python", "api.py"]

