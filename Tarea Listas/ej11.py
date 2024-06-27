notas = []
notasUnicas = []
cantidadNotas = []

nota = input("Ingrese nota: ").upper()
    
for n in nota.split(","):
    notas.append(n)
print(notas)

for i in notas:
    if i not in notasUnicas:
        notasUnicas.append(i)
        cantidadNotas.append(1)
    else:
        indice = notasUnicas.index(i)
        cantidadNotas[indice] += 1
    
print(notasUnicas)
print(cantidadNotas)
    
    