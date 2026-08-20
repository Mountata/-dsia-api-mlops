# Image de base légère
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /code

# Copie uniquement du fichier de dépendances d'abord (meilleur cache Docker)
COPY requirements.txt .

# Installation des dépendances (sans cache pip pour alléger l'image)
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application
COPY app/ ./app/

# Port exposé par Uvicorn/FastAPI
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
