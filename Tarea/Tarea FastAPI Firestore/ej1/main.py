import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException

app = FastAPI()

cred = credentials.Certificate('ej1/t2ej1-155b0-firebase-adminsdk-cwdrq-608cccdafd.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

@app.get("/horarios")
def consulta():
    datos = db.collection('Horario').get()
    data = [{i.id:i.to_dict()} for i in datos]
    return data

@app.get("/tarifas")
def consulta():
    datos = db.collection('Tarifas').get()
    data = [{i.id:i.to_dict()} for i in datos]
    return data

@app.get("/info")
def consulta():
    datos = db.collection('Info').get()
    data = [{i.id:i.to_dict()} for i in datos]
    return data

@app.get("/info/{id}")
def consulta_id(id: str):
    doc = db.collection('Info').document(id).get()
    if doc.exists:
        return {doc.id: doc.to_dict()}
    else:
        raise HTTPException(status_code=404, detail="Documento no encontrado")