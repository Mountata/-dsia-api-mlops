"""
API FastAPI - Catalogue de produits high-tech
M1 DSIA - Projet MLOps
"""

import json
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ---------------------------------------------------------------------------
# Configuration de l'application
# ---------------------------------------------------------------------------

APP_VERSION = "1.0.0"
DATA_FILE = Path(__file__).parent / "data.json"

app = FastAPI(
    title="Catalogue Produits API",
    description="API exposant un catalogue de produits high-tech depuis un fichier JSON",
    version=APP_VERSION,
)


# ---------------------------------------------------------------------------
# Modèles de données
# ---------------------------------------------------------------------------

class Item(BaseModel):
    id: int
    nom: str
    categorie: str
    prix: float
    stock: int


# ---------------------------------------------------------------------------
# Chargement des données
# ---------------------------------------------------------------------------

def load_items() -> List[dict]:
    """Charge les items depuis le fichier data.json."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Fichier de données introuvable : {DATA_FILE}")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("items", [])


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", tags=["Général"])
def read_root():
    """Message de bienvenue et version de l'API."""
    return {
        "message": "Bienvenue sur l'API Catalogue Produits",
        "version": APP_VERSION,
    }


@app.get("/health", tags=["Général"])
def health_check():
    """Vérifie que l'API est opérationnelle."""
    return {"status": "ok"}


@app.get("/items", response_model=List[Item], tags=["Items"])
def get_items():
    """Retourne tous les enregistrements du catalogue."""
    items = load_items()
    return items


@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int):
    """Retourne un enregistrement par son identifiant."""
    items = load_items()
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item avec id={item_id} introuvable")
