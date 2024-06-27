datos = {}
clave = ""
def AgregarValor(clave, valor):
    datos[clave] = valor
    
for i in range(5):
    while True:
        clave = input(f"Ingrese clave {i + 1}: ")
        if not(clave in datos):
            datos[clave] = ""
            break
        else:
            print("Clave ya existe")
        

x = True
while x:
    print("----MENU----")
    print("1. Consultar diccionario.")
    print("2. Agregar valor a clave. ")
    print("3. Eliminar clave. ")
    print("4. Agregar dato.")
    print("5. Buscar")
    print("6. Salir")
    
    r = input("Elija su Opcion: ")
    if r == "1":
        for c, v in datos.items():
            print(f"{c}: {v}")
    elif r == "2":
        r = input("Que clave desea editar: ")
        if r in datos:
            datos[r] = input("Ingrese nuevo valor: ")
        else:
            print("Clave no en diccionario.")
    elif r == "3":
        r = input("Que clave desea eliminar: ")
        if r in datos:
            del datos[r]
        else:
            print("Clave no en diccionario.")
    elif r == "4":
        while True:
            clave = input(f"Ingrese nueva clave: ")
            if not(clave in datos):
                valor = input(f"Ingrese el valor de {clave}: ")
                break
            else:
                print("Clave ya existe")
    
        AgregarValor(clave, valor)
    elif r == "5":
        y = True
        while y:
            valor = input(f"Ingrese valor a buscar: ")
            for v in datos.values():
                if v == valor:
                    print("Si se encuentra.")
                    y = False
    elif r == "6":
        break
    else:
        print("Opcion no valida")
                    