cantidad = int(input("Ingrese la cantidad de datos que desea agregar: "))
datos = {}
for i in range(cantidad):
    while True:
        clave = input(f"Ingrese clave {i + 1}: ")
        if not(clave in datos):
            valor = input(f"Ingrese el valor de {clave}: ")
            break
        else:
            print("Clave ya existe")
    
    datos[clave] = valor
    
for c,v in datos.items():
    print(f"{c}: {v}")



 