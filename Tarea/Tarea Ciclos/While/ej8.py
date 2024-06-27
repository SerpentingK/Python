import time
while True:
    n = int(input("Ingrese el numeor que desea multiplicar: \n"))
    x = int(input("Ingrese desde que numeor desea la tabla de multiplicar:\n"))
    y = int(input("Ingrese hasta que numero desea la tabla de multiplicar:\n"))
    for i in range(x, y + 1):
        print(f"{i} x {n} = {i * n}")
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break