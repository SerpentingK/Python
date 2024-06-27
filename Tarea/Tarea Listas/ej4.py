import random

# Inicialización de la lista con 10 valores aleatorios entre 1 y 100
lista = []
for _ in range(10):
    lista.append(random.randint(1, 100))
print("Lista original:", lista)

# Ordenamiento personalizado
n = len(lista)
for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Lista ordenada:", lista)
