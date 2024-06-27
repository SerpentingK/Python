datos = {
    "Nombre" : "David",
    "Edad" : 19,
    "Programa": "ADSO",
    "Correos": ["davcr@gmail.com", "davcr2@gmail.com"]
}
print(datos["Nombre"])
print(datos["Correos"][0])
print(datos["Correos"][1])
print(datos.values())
print(datos.keys())

datos["Nombre"] = "Juan"
datos["Celular"] = "3203169321"
print(datos)

del datos["Celular"]
print(datos)

base ={
    1: {
    "Nombre" : "David",
    "Edad" : 19,
    "Programa": "ADSO",
    "Correos": ["davcr@gmail.com", "davcr2@gmail.com"]
    },
    2: {
    "Nombre" : "Juan",
    "Edad" : 19,
    "Programa": "ADSO",
    "Correos": ["davcr@gmail.com", "davcr2@gmail.com"]
    },
    3: {
    "Nombre" : "Pedro",
    "Edad" : 19,
    "Programa": "ADSO",
    "Correos": ["davcr@gmail.com", "davcr2@gmail.com"]
    },
}


for c,v in base.items():
    print(f"Usuario {c}: ")
    for x, y in v.items():
        print(f"{x}: {y}")
