# Catalogue Produits API — Projet MLOps M1 DSIA

## 1. Description du projet

Ce projet expose, via une API REST développée avec **FastAPI**, un catalogue de **produits high-tech** (informatique, accessoires, audio, stockage, réseau...). Les données proviennent d'un fichier `data.json` contenant 12 enregistrements structurés (id, nom, catégorie, prix, stock).

L'API est conteneurisée avec **Docker** et publiée sur **Docker Hub**.

**Membres du groupe (groupe_khadim) :**
- René Legrand Mountata
- Khadim GUEYE
- André Ibrahima SENE

---

## 2. Structure du projet

mon_projet/
├── app/
│ ├── main.py # application FastAPI
│ └── data.json # fichier de données
├── screenshots/ # captures d'écran build/run/test
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md






---

## 3. Description des routes

| Méthode | URL              | Description                              | Exemple de réponse |
|---------|-------------------|-------------------------------------------|----------------------|
| GET     | `/`               | Message de bienvenue + version de l'API   | `{"message": "Bienvenue sur l'API Catalogue Produits", "version": "1.0.0"}` |
| GET     | `/health`         | Statut de l'API                           | `{"status": "ok"}` |
| GET     | `/items`          | Retourne tous les enregistrements         | `[{"id": 1, "nom": "Ordinateur portable Pro 14", ...}, ...]` |
| GET     | `/items/{id}`     | Retourne un enregistrement par son id     | `{"id": 1, "nom": "Ordinateur portable Pro 14", ...}` (404 si id inexistant) |

La documentation interactive est disponible automatiquement sur `/docs` (Swagger UI) et `/redoc`.

---

## 4. Prérequis

- Docker installé ([docker.com](https://docs.docker.com/get-docker/))
- Python 3.11 (uniquement pour un test en local sans Docker)
- Un compte Docker Hub ([hub.docker.com](https://hub.docker.com))

---

## 5. Lancer l'API en local (sans Docker)

```bash
python3 -m venv venv
source venv/bin/activate      # sous Windows : venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

L'API est accessible sur `http://localhost:8000` et la doc sur `http://localhost:8000/docs`.

---

## 6. Build et run avec Docker

### Build de l'image

```bash
docker build -t mon-api:latest .
```

![Build Docker](screenshots/build.png)

### Run du conteneur

```bash
docker run -d -p 8000:8000 --name catalogue-api mon-api:latest
```

Vérification du conteneur actif :

![docker ps](screenshots/ps.png)

Vue du conteneur dans Docker Desktop :

![Docker Desktop containers](screenshots/containers.png)

### Test des routes via Swagger UI (`/docs`)

Test de `GET /items` :

![Test GET items](screenshots/items.png)

Test de `GET /items/1` :

![Test GET items/1](screenshots/item1.png)

---

## 7. Publication sur Docker Hub

```bash
# Authentification
docker login

# Tag de l'image locale
docker tag mon-api:latest mountata/dsia-api:v1.0

# Push vers Docker Hub
docker push mountata/dsia-api:v1.0
```

![Docker push](screenshots/push.png)

**Lien public de l'image Docker Hub :**
👉 https://hub.docker.com/r/mountata/dsia-api

### Pull et run depuis Docker Hub (vérification)

```bash
docker pull mountata/dsia-api:v1.0
docker run -d -p 8000:8000 mountata/dsia-api:v1.0
```

---

## 8. Ressources

- Documentation FastAPI : https://fastapi.tiangolo.com
- Documentation Docker : https://docs.docker.com
- Docker Hub : https://hub.docker.com