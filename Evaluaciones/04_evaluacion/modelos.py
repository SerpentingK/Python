from pydantic import BaseModel as bm

class paciente(bm):
    codigo:str
    nombre:str
    edad:int    
    fecha_nacimineto:str
    fecha_consulta:str
    