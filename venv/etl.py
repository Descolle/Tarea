import os
import requests
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
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


#Extracción de datos
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
response = requests.get(url)
json_data = response.json()

cards = json_data["data"]

print ("cartas extraidas",len(cards))

#Tranformación de datos
#HENSHIN!!!!

df = pd.DataFrame(cards)
df = df [[
    "id",
    "name",
    "type",
    "race",
    "atk",
    "def",
    "level",
    "attribute",
]]

#reemplazara todos los atk ? (NaN) por 0
df [["atk", "def","level"]] = df [["atk", "def","level"]].fillna(0)
df["attribute"] = df["attribute"].fillna("None") #reemplazamos los atributos nulos por "None"

print(df.head())

#Elimina la carga previa de datos para evitar duplicados
collection.delete_many({})
print("Colección limpiada")


#Carga de datos
records = df.to_dict(orient="records")
collection.insert_many(records)
print("Datos cargados en MongoDB Atlas")


