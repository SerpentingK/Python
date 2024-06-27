from fastapi import FastAPI
import random
import string
app = FastAPI()

@app.get("/")
def root():
    return "Crea un servicio que reciba un rango de números (inicio y fin) como parámetros en la URL y devuelva una lista de los números primos dentro de ese rango."

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

@app.get("/{i}/{f}")
def primos_en_rango(i:int, f:int):
    primos = []
    for numero in range(i, f + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos