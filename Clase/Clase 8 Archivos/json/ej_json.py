import json

mis_datos = {
    "Nombre": "Juan",
    "Apellido" : "Perez",
    "Edad" : 30,
    "Ciudad": "Bogota"
}

datos = "Datos.json"    

with open(datos, "w") as archivo:
    json.dump(mis_datos, archivo)
    
print(f"Los datos se han escrito en '{datos}'")