import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
app = FastAPI()

cred = credentials.Certificate('ej2/t2ej2-90e2e-firebase-adminsdk-v8kbn-57183f356d.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

class Ave(BaseModel):
    etapa: str
    fecha: str
    lote: str
    alimento: list


@app.get("/aves")
def consulta():
    datos = db.collection('aves').get()
    data = [{i.id:i.to_dict()} for i in datos]
    return data
@app.get("/aves/{id}")
def consulta_id(id: str):
    doc = db.collection('aves').document(id).get()
    if doc.exists:
        return {doc.id: doc.to_dict()}
    else:
        raise HTTPException(status_code=404, detail="Ave no encontrado")

@app.get("/lote/{n}")
def consulta_lote(n: str):
    datos = db.collection('aves').where('lote', '==', n).get()
    data = {i.id: i.to_dict() for i in datos}
    return data

@app.get("/etapa/{e}")
def consulta_lote(e: str):
    datos = db.collection('aves').where('etapa', '==', e).get()
    data = {i.id: i.to_dict() for i in datos}
    return data

@app.get("/alimento/{alimento}")
def consulta_alimento(alimento: str):
    datos = db.collection('aves').where('alimento', 'array_contains', alimento).get()
    data = {i.id: i.to_dict() for i in datos}
    return data


@app.post("/aves/{id}", response_model=Ave)
def agrega_ave(id: str, ave: Ave):
    doc_ref = db.collection('aves').document(id)
    if doc_ref.get().exists:
        raise HTTPException(status_code=400, detail="Documento con ese ID ya existe")
    
    doc_ref.set(ave.dict())
    return {"id": id, "message": "Ave agregada exitosamente"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
