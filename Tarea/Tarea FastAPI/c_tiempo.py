from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return"Implementa un algoritmo que reciba la distancia a recorrer (en kilómetros) y la velocidad media (en kilómetros por hora) como parámetros en la URL, y calcule el tiempo estimado de viaje."

@app.get("/{d}/{v}")
def CalculoTiempoViaje(d:float, v:float):
    t = d/v
    return (f"Tiempo: {round(t, 2)} Horas")