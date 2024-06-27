import time

for _ in range(5):  # Repetir 5 veces, puedes cambiar el número según lo necesites
    mayus = -99999
    minus = 99999

    cantidad = int(input("Ingrese que cantidad de números desea ingresar:\n "))
    for i in range(cantidad):
        n = int(input(f"Ingrese número {i + 1}: \n"))
        if mayus < n:
            mayus = n
        if minus > n:
            minus = n
    print(f"El número mayor es: {mayus}")
    print(f"El número menor es: {minus}")
    r = input("¿Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
