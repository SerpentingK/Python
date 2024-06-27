
numeros = []

while True:
    # Solicitar números al usuario hasta que se ingrese un número negativo
    while True:
        numero = int(input("Introduce un número (negativo para terminar): "))
        if numero < 0:
            break
        numeros.append(numero)

    # Imprimir la lista con los elementos introducidos
    print("Elementos introducidos:")
    for num in numeros:
        print(num)
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        break
