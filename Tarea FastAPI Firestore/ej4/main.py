import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

cred = credentials.Certificate('ej4/t2ej4-543db-firebase-adminsdk-1ma8l-a8eb5e15e7.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.get("/estudiantes")
def default():
    estudiantes = db.collection('Estudiantes').get()
    return [{estudiante.id: estudiante.to_dict()} for estudiante in estudiantes]

@app.get("/profesores")
def default():
    profesores = db.collection("Profesores").get()
    return [{p.id: p.to_dict()} for p in profesores]
