list = []
list2 = []
x = int(input("Ingrese cantidad de numeros: "))
for i in range(x):
    new = int(input(f"Ingrese el numero {i + 1}: "))
    list.append(new)
for i in list:
    num = i
    total = 0
    cantidad = 0
    for j in list:
        if j == i:
            total += j
            cantidad += 1
    if not(i in list2):
        print(f"Del numero {i} hay {cantidad} y su suma es: {total}")
        
    list2.append(i)
        