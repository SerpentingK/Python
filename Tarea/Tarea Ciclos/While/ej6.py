import time

mayus = -99999
minus = 99999

while True:
    cantidad = int(input("Ingrese que cantidad de numeros desea ingresar:\n "))
    for i in range(cantidad):
        n = int(input(f"Ingrese numero {i + 1}: \n"))
        if mayus < n:
            mayus = n
        elif minus > n:
            minus = n
    print(f"El numero mayor es: {mayus}")
    print(f"El numero menor es: {minus}")
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break

