c = int(input("Ingre cantidad de palabras: "))
lista = []
for i in range(c):
    n = input(f"Ingrese palabras {i + 1}: ")
    lista.append(n)
    
def repetidas(lista):
    nl = []
    for i in lista:
        if i not in nl:
            nl.append(i)
    return nl

print(repetidas(lista))
            