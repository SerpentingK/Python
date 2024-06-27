from fastapi import FastAPI,HTTPException
from modelos import paciente
import json


app = FastAPI()

base = []
ruta = 'base.json'

def cargarDatos():
    try:
        with open(ruta, 'r') as f:
            datos = json.load(f)
            for dato in datos:
                base.append(paciente(**dato))
    except Exception:
        
        pass
        
cargarDatos()

def reescribirDatos():
    with open(ruta, 'w') as f:
        json.dump([j.dict() for j in base], f, indent=4)
        
@app.get("/pacientes")
async def default():
    reescribirDatos()
    if len(base) == 0:
        raise HTTPException(status_code=404, detail="Lista Vacia")
    else:
        return base
    
@app.get("/pacientes/{id}")
async def search_for_id(id:str):
    for i in base:
        if i.codigo == id:
            return i
    raise HTTPException(status_code=404, detail="Paciente no encontrado")

@app.post("/pacientes", response_model=paciente)
async def add_paciente(p:paciente):
    for i in base:
        if i.codigo == p.codigo:
            raise HTTPException(status_code=409, detail="Codigo ya existente")
    base.append(p)
    reescribirDatos()
    return p
@app.put("/pacientes/{id}", response_model=paciente)
async def update_paciente(id:str, p:paciente):
    for i in base:
        if i.codigo == p.codigo:
            i = p
            reescribirDatos()
            return i
    raise HTTPException(status_code=404, detail="Codigo no encontrado")

@app.put("/pacientes/{id}/edad/{edad}")
async def update_edad(id:str, edad:int):
    encontrado = False
    for i in base:
        if i.codigo == id:
            encontrado = True
            i.edad = edad
            reescribirDatos()
            return i
    if not(encontrado):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")


@app.put("/pacientes/{id}/fecha/{fecha}")
async def update_fecha(id:str, fecha:str):
    encontrado = False
    for i in base:
        if i.codigo == id:
            encontrado = True
            i.fecha_consulta = fecha
            reescribirDatos()
            return i
    if not(encontrado):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
@app.delete("/pacientes/{id}")
async def delete_paciente(id:str):
    encontrado = False
    for i in base:
        if i.codigo == id:
            encontrado = True
            base.remove(i)
            reescribirDatos()
    if not(encontrado):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
@app.get("/pacientes/nombre/{nombre}")
async def consulta_nombre(nombre:str):
    lista = []
    for i in base:
        if i.nombre.lower() == nombre.lower():
            lista.append(i)
            
    return lista

@app.get("/pacientes/edad/{edad}")
async def consulta_edad(edad:int):
    lista = []
    for i in base:
        if i.edad == edad:
            lista.append(i)
            
    return lista

@app.get("/pacientes/fecha/{fecha}")
async def consulta_fecha(fecha:str):
    lista = []
    for i in base:
        if i.fecha_consulta == fecha:
            lista.append(i)
            
    return lista

@app.get("/total")
def consulta_total():
    print(1)
    return {"Total Pacientes": len(base)}
