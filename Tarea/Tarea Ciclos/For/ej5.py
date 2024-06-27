import time

for _ in range(5):  # Repetir 5 veces, puedes cambiar el número según lo necesites
    x = True
    n = 0
    while x:
        n = int(input("Ingrese el número del cual quiere saber el factorial: \n"))
        if n <= 0:
            print("Valor inválido, ingrese un número entero positivo")
        else:
            x = False
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f"El factorial de {n} es: {f}")
    r = input("¿Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
