numbers = []
pares = []
inpares = []
negativos = []

cantidad = int(input("Ingrese que cantidad de numeros desea ingresar: "))
for i in range(cantidad):
    new = int(input(f"Ingrese el numero {i + 1}: "))
    numbers.append(new)
    if new % 2 == 0:
        pares.append(new)
    else:
        inpares.append(new)
    if new < 0:
        negativos.append(new)

print(f"Numeros ingresados: {numbers}")
print(f"Pares: {pares}")
print(f"Inpares: {inpares}")
print(f"Negativos: {negativos}")