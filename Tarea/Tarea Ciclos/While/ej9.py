import time
while True:
    limite_tablas = int(input("Ingrese el número hasta el cual desea calcular las tablas de multiplicar: "))
    limite_multiplicador = int(input("Ingrese el número hasta el cual desea multiplicar en cada tabla: "))

    for i in range(1, limite_tablas + 1):
        print(f"Tabla de multiplicar del {i}:")
        for j in range(1, limite_multiplicador + 1):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print()
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break
