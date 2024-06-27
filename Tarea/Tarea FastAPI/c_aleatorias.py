from fastapi import FastAPI
import random
import string
app = FastAPI()

@app.get("/")
def root():
    return "Desarrolla un servicio que reciba la longitud deseada de la contraseña como parámetro en la URL y genere una contraseña aleatoria de esa longitud."

@app.get("/{l}")
def generarContraseña(l: int):
    chars = string.ascii_letters + string.digits
    c = ""
    for i in range(l):
        c += random.choice(chars)
        
    return {"Contraseña: ": c}