import os
import requests
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Obtener credenciales desde variables de entorno
user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
cluster = os.getenv("MONGO_CLUSTER")

uri = f"mongodb+srv://{user}:{password}@{cluster}/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client["yugioh_db"]
collection = db["cards"]

app = FastAPI()

#Endpoint para obtener todas las cartas
@app.get("/")
def read_root():
    return {"mensaje": "API ygo Funcionando"}

@app.get("/cards")
def get_cards(limit: int = 50):
    cards = list(collection.find({}, {"_id": 0}).limit(limit)) #excluimos el campo _id
    return cards

@app.get("/stats/avg-atk")
def get_avg_atk():
    pipeline = [
        {"$group": {"_id": None, "avg_atk": {"$avg": "$atk"}}}
    ]
    result = list(collection.aggregate(pipeline))
    return result[0] if result else {"avg_atk": 0}

@app.get("/stats/by-type")
def get_cards_by_type():
    pipeline = [
        {"$group": {"_id": "$type", "count": {"$sum": 1}}}
    ]
    result = list(collection.aggregate(pipeline))
    return result

@app.get("/stats/attribute-distribution")
def get_cards_by_attribute():
    pipeline = [
        {"$group": {"_id": "$attribute", "count": {"$sum": 1}}} #agrupamos x id y atributo y contamos cuantos hay de cada atributo
    ]
    result = list(collection.aggregate(pipeline))
    return result

#para que corar uvicorn <api:app --reload>
# ctrl + c para detener el servidor
#deactivate para salir del entorno virtual