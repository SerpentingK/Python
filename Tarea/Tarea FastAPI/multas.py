from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return "Ingrese los datos del tramo: distancia (km), tiempo (minutos), velocidad máxima permitida (km/h). Ejemplo: /10/5/110"

@app.get("/{distancia}/{tiempo}/{velocidad_maxima}")
def verificar_infraccion(distancia: float, tiempo: float, velocidad_maxima: float):
    # Validaciones
    if distancia <= 0 or tiempo <= 0 or velocidad_maxima <= 0:
        raise HTTPException(status_code=400, detail="Todos los valores deben ser positivos y mayores que cero.")
    
    # Convertir tiempo a horas para calcular la velocidad media
    tiempo_horas = tiempo / 60
    
    # Calcular la velocidad media
    velocidad_media = distancia / tiempo_horas
    
    # Determinar si debe ser multado
    multado = velocidad_media > velocidad_maxima
    
    return {
        "distancia": distancia,
        "tiempo": tiempo,
        "velocidad_maxima": velocidad_maxima,
        "velocidad_media": round(velocidad_media, 2),
        "multado": multado,
        "mensaje": "Debe ser multado" if multado else "No debe ser multado"
    }
