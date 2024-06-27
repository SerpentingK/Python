import time

while True:
    x = True
    n = 0
    while x:
        n = int(input("Ingrese el numero del cual quiere saber el factorial: \n"))
        if n <= 0:
            print("Valor invalido, ingrese numeor entero positivo")
        else:
            x = False
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f)
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break
        