import time

for _ in range(5):  # Repetir 5 veces, puedes cambiar el número según lo necesites
    total = 0

    for i in range(10):
        total += int(input(f"Ingrese número {i + 1}: \n"))

    promedio = total / 10

    print(f"El promedio es {promedio}")
    r = input("¿Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
