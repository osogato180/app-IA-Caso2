from pymongo import MongoClient
import os

def get_db():
    # Puedes usar variable de entorno o pegar tu URI directo
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    
    client = MongoClient(MONGO_URI)
    db = client["banco_regional_andino"]
    return db