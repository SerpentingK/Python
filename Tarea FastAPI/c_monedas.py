from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Ejercicio 2": "Crea un servicio que reciba la cantidad a convertir y las monedas de origen y destino como parámetros en la URL, y devuelva la cantidad convertida"}

@app.get("/{c}/{m_origen}/{m_destino}")
async def ConvertirMonedas(c: float, m_origen: float, m_destino: float):
    c_base = c / m_origen
    c_total = round(c_base * m_destino,2)
    return {"Su conversion de monedas es":c_total}