import time

while True:
    total = 0

    for i in range(0,10):
        total += int(input(f"Ingrese numero {i + 1}: \n"))

    promedio = total/10

    print(f"El promedio es {promedio}")
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break
