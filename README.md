# Catalogue Produits API — Projet MLOps M1 DSIA

## 1. Description du projet

Ce projet expose, via une API REST développée avec **FastAPI**, un catalogue de **produits high-tech** (informatique, accessoires, audio, stockage, réseau...). Les données proviennent d'un fichier `data.json` contenant 12 enregistrements structurés (id, nom, catégorie, prix, stock).

L'API est conteneurisée avec **Docker** et publiée sur **Docker Hub**.

**Membres du groupe_khadim : **
- René legrand mountata
- Khadim GUEYE
- André Ibrahima SENE

>

---

## 2. Structure du projet

```
mon_projet/
├── app/
│   ├── main.py        # application FastAPI
│   └── data.json       # fichier de données
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 3. Description des routes

| Méthode | URL              | Description                              | Exemple de réponse |
|---------|-------------------|-------------------------------------------|----------------------|
| GET     | `/`               | Message de bienvenue + version de l'API   | `{"message": "Bienvenue sur l'API Catalogue Produits", "version": "1.0.0"}` |
| GET     | `/health`         | Statut de l'API                           | `{"status": "ok"}` |
| GET     | `/items`          | Retourne tous les enregistrements         | `[{"id": 1, "nom": "Ordinateur portable Pro 14", "categorie": "Informatique", "prix": 1299.99, "stock": 12}, ...]` |
| GET     | `/items/{id}`     | Retourne un enregistrement par son id     | `{"id": 1, "nom": "Ordinateur portable Pro 14", "categorie": "Informatique", "prix": 1299.99, "stock": 12}` (404 si id inexistant) |

La documentation interactive est disponible automatiquement sur `/docs` (Swagger UI) et `/redoc`.

---

## 4. Prérequis

- Docker installé ([docker.com](https://docs.docker.com/get-docker/))
- Python 3.11 (uniquement pour un test en local sans Docker)
- Un compte Docker Hub ([hub.docker.com](https://hub.docker.com))

---

## 5. Lancer l'API en local (sans Docker)

```bash
# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate      # sous Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

L'API est alors accessible sur `http://localhost:8000` et la doc sur `http://localhost:8000/docs`.

---

## 6. Build et run avec Docker

### Build de l'image

```bash
docker build -t mon-api:latest .
```

### Run du conteneur

```bash
docker run -d -p 8000:8000 --name catalogue-api mon-api:latest
```

### Test

```bash
curl http://localhost:8000/health
curl http://localhost:8000/items
curl http://localhost:8000/items/1
```

Sortie attendue pour `/health` :
```json
{"status": "ok"}
```

---

## 7. Publication sur Docker Hub

```bash
# Authentification
docker login

# Tag de l'image locale
docker tag mon-api:latest <votre-username>/dsia-api:v1.0

# Push vers Docker Hub
docker push <votre-username>/dsia-api:v1.0
```

**Lien public de l'image Docker Hub :**
👉 `https://hub.docker.com/r/mountata/dsia-api`

 **Public**.

### Pull et run depuis Docker Hub (vérification)

```bash
docker pull <votre-username>/dsia-api:v1.0
docker run -d -p 8000:8000 <votre-username>/dsia-api:v1.0
```

---

## 8. Ressources

- Documentation FastAPI : https://fastapi.tiangolo.com
- Documentation Docker : https://docs.docker.com
- Docker Hub : https://hub.docker.com
