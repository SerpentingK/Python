from pydantic import BaseModel as BM

class credito(BM):
    id:str
    doc:str
    nombre:str
    apellido:str
    email:str
    tel:str
    edad:int
    monto:float
    fecha:str
    saldo:float
    estado:str
    linea:str
    
    
    