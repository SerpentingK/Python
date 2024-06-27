while True:
    # Declarar tres listas vacías
    lista1 = []
    lista2 = []
    lista3 = []

    # Solicitar valores para lista1
    print("Introduce 5 valores para la lista1:")
    for i in range(5):
        valor = int(input(f"Valor {i + 1}: "))
        lista1.append(valor)

    # Solicitar valores para lista2
    print("Introduce 5 valores para la lista2:")
    for i in range(5):
        valor = int(input(f"Valor {i + 1}: "))
        lista2.append(valor)

    # Calcular lista3 = lista1 + lista2
    for i in range(5):
        suma = lista1[i] + lista2[i]
        lista3.append(suma)

    # Imprimir lista3
    print("La lista3 resultante de la suma de lista1 y lista2 es:")
    print(lista3)

    r = input("Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        break
