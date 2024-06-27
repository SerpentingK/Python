from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"Ejercicio uno: " : "Desarrolla un servicio que reciba el peso (en kilogramos) y la altura (en metros como parametro.)"}

@app.get("/{peso}/{altura}")
async def CalcularIMC(peso:int, altura:float):
    alturaCuadrada = altura**2
    indice_masa_corporal = peso/alturaCuadrada
    return {"Tu IMC es: ": indice_masa_corporal}
    
    