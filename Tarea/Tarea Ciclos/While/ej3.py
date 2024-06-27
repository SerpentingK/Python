import time

while True:
    x = True
    cantidad = 0
    while x:
        cantidad = int(input("Ingrese que cantidad de numeros desea ingresar: \n"))
        if cantidad <= 0:
            print("Valor invalido, ingrese de nuevo")
        else:
            x = False

    total = 0
    for i in range(cantidad):
        total += int(input(f"Ingrese el numero {i + 1}:\n"))
    promedio = total/cantidad

    print(f"El promedio es {promedio}")
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break
