import time

for _ in range(5):  # Repetir 5 veces, puedes cambiar el número según lo necesites
    x = True
    cantidad = 0
    while x:
        cantidad = int(input("Ingrese que cantidad de números desea ingresar: \n"))
        if cantidad <= 0:
            print("Valor inválido, ingrese de nuevo")
        else:
            x = False

    total = 0
    for i in range(cantidad):
        total += int(input(f"Ingrese el número {i + 1}:\n"))
    promedio = total / cantidad

    print(f"El promedio es {promedio}")
    r = input("¿Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
