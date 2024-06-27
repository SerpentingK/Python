list = []
tels = []
tel = ""
x = int(input("Ingrese cantidad de usuarios: "))
for i in range(x):
    nombre = input("Ingrese su nombre: ")
    list.append(nombre)
    for j in range(2):
        tel = input(f"Ingrese numero de telefono {j + 1} de {nombre}: ")
    tels.append(tel)
buscar = input("Ingrese usuario a buscar: ")
for i in list:
    if i == buscar:
        print(f"Numero: {tels[list.index(i)]}")


