lista = []
while True:
    nuevo = int(input("Ingrese un numero a agregar, numero negativo para terminar: "))
    if nuevo < 0:
        break
    lista.append(nuevo)
print(lista)

lista_sin_duplicados = []

for num in lista:
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)

print("Lista sin duplicados:", lista_sin_duplicados)