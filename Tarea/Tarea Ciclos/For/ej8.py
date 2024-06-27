import time

for _ in range(10):  # Cambiar el rango según sea necesario
    n = int(input("Ingrese el número que desea multiplicar: \n"))
    x = int(input("Ingrese desde qué número desea la tabla de multiplicar:\n"))
    y = int(input("Ingrese hasta qué número desea la tabla de multiplicar:\n"))
    for i in range(x, y + 1):
        print(f"{i} x {n} = {i * n}")
    r = input("¿Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
