from fastapi import FastAPI, HTTPException
from modelos import credito  # Asegúrate de que los modelos están definidos correctamente
import json

app = FastAPI()

lineas_de_credito = ["compra de vehiculo", "libre inversion", "compra de cartera", "estudio", "vacaciones"]
base = []

# Carga inicial de datos desde el archivo JSON
def cargarDatos():
    try:
        with open('creditos.json', 'r') as f:
            datos = json.load(f)
            for dato in datos:
                base.append(credito(**dato))  # Correción: Desempaquetar correctamente los datos en el modelo
    except FileNotFoundError:
        pass

cargarDatos()

def reescribirDatos():
    with open('creditos.json', 'w') as f:
        json.dump([j.dict() for j in base], f, indent=4)

@app.get("/creditos")
async def default():
    reescribirDatos()
    if len(base) == 0:
        raise HTTPException(status_code=404, detail="Lista vacia")
    else:
        return base

# Correción: Cambiado el nombre del parámetro a "id" para evitar confusión
@app.get("/creditos/{id}")
async def search_for_id(id: str):
    for i in base:  
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail="Credito no encontrado")

@app.post("/creditos", response_model=credito)
async def addCredito(c: credito):
    count = 0
    for i in base:
        if c.id == i.id:
            raise HTTPException(status_code=409, detail="Id ya existente")  # Correción: Usar 409 para conflicto
    for i in base:
        if c.doc == i.doc and i.estado == "activo":
            count += 1
        if count == 2:
            raise HTTPException(status_code=400, detail="Cliente con ya 2 creditos activos")  # Correción: Usar 400 para solicitud inválida
    if c.linea not in lineas_de_credito:
        raise HTTPException(status_code=400, detail="Linea de credito invalida")  # Correción: Usar 400 para solicitud inválida
    base.append(c)
    reescribirDatos()
    return c

@app.put("/creditos/{id}", response_model=credito)
async def updateCredito(id: str, credito: credito):
    for i, c in enumerate(base):
        if c.id == id:
            if c.edad == credito.edad and c.fecha == credito.fecha:
                base[i] = credito
                reescribirDatos()
                return credito
            else:
                raise HTTPException(status_code=400, detail="Edad y fecha no modificables.")  # Correción: Usar 400 para solicitud inválida
    raise HTTPException(status_code=404, detail="Ningun credito activo con esta id.")  # Correción: Posicionar correctamente la excepción

@app.delete("/creditos/{id}")
async def deleteCredito(id: str):
    for i in base:
        if i.id == id:
            if i.saldo == 0:
                base.remove(i)
                reescribirDatos()
                return {"detail": "Credito eliminado"}  # Correción: Devolver mensaje en vez de lanzar excepción
            else:
                raise HTTPException(status_code=400, detail="Saldo debe ser igual a 0")  # Correción: Usar 400 para solicitud inválida
    raise HTTPException(status_code=404, detail="ID no encontrada")

@app.get("/creditos/menoresEdad")
async def consultaMenores():
    l = [i for i in base if i.edad <= 25]  # Correción: Simplificar usando comprensión de listas
    if len(l) == 0:
        raise HTTPException(status_code=404, detail="Ninguno encontrado")
    else:
        return l

@app.get("/creditos/mayoresEdad")
async def consultaMayores():
    l = [i for i in base if i.edad >= 60]  # Correción: Simplificar usando comprensión de listas
    if len(l) == 0:
        raise HTTPException(status_code=404, detail="Ninguno encontrado")
    else:
        return l

@app.get("/creditos/menoresMonto")
async def consultaMenoresMonto():
    l = [i for i in base if i.monto <= 5000000]  # Correción: Simplificar usando comprensión de listas
    if len(l) == 0:
        raise HTTPException(status_code=404, detail="Ninguno encontrado")
    else:
        return l

@app.get("/creditos/mayoresMonto")
async def consultaMayoresMonto():
    l = [i for i in base if i.monto >= 10000000]  # Correción: Simplificar usando comprensión de listas
    if len(l) == 0:
        raise HTTPException(status_code=404, detail="Ninguno encontrado")
    else:
        return l

@app.get("/creditos/fecha/{fecha}")
async def consultaFecha(fecha: str):
    l = [i for i in base if i.fecha == fecha]  # Correción: Simplificar usando comprensión de listas
    if len(l) == 0:
        raise HTTPException(status_code=404, detail="Ninguno encontrado")
    else:
        return l

@app.get("/creditos/doc/{doc}")
async def consultaDoc(doc: str):
    l = [i for i in base if i.doc == doc]
    total = sum(i.monto for i in l)  # Correción: Simplificar usando sum()
    if len(l) == 0:
        raise HTTPException(status_code=404, detail="Ninguno encontrado")
    else:
        l.append({"Total: ": total})  # Correción: Devolver total como parte de la lista
        return l

@app.get("/creditos/total")
async def consultaTotal():
    total = sum(i.monto for i in base if i.estado == "activo")  # Correción: Simplificar usando sum()
    return {"TOTAL CREDITOS": total}
