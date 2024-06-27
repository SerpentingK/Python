datos = dict()

def personaMenor(datos):
    nombre = str()
    edadMenor = -9999
    for i in datos:
        if datos[i] > edadMenor:
            nombre = i
            edadMenor = datos[i]
    return nombre

c = int(input("Ingrese cantidad de personas: "))
for i in range(c):
    n = input(f"Ingrese nombre persona {i + 1}: ")
    e = int(input(f"Ingrese edad persona {i + 1}: "))
    datos[n] = e
print(datos)
print(personaMenor(datos))