# Preguntar al usuario la raza del perro y el puesto obtenido
while True:
    raza = input("Ingrese la raza del perro: ").upper()
    if raza == "PITBULL":
        valor_base = 6000000
        break
    elif raza == "BULY":
        valor_base = 6500000
        break
    elif raza == "ROTTWHILLER":
        valor_base = 4000000
        break
    elif raza == "LABRADOR RETRIEVER":
        valor_base = 3500000
        break
    elif raza == "GOLDEN RETRIEVER":
        valor_base = 3500000
        break
    elif raza == "DOBERMAN":
        valor_base = 5000000
        break
    elif raza == "DOGO ARGENTINO":
        valor_base = 5500000
        break
    else:
        print("Raza no válida.")
while True:
    puesto = int(input("Ingrese el puesto obtenido (1, 2 o 3): "))
    if puesto == 1 or puesto == 2 or puesto == 3:
        break
    else:
        print("Puesto invalido")

# Calcular el nuevo valor del perro según el puesto obtenido
if puesto == 1:
    nuevo_valor = valor_base * 2
elif puesto == 2:
    nuevo_valor = valor_base + 800000
elif puesto == 3:
    nuevo_valor = valor_base + 200000

# Mostrar el nuevo valor del perro
print(f"El nuevo valor del perro {raza} es: ${nuevo_valor}")
