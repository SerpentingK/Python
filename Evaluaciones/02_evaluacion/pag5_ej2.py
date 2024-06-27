termino = 50
lista = [0,1]
while True:
    lista.append(lista[-1] + lista[-2])
    if lista[-1] >= termino:
        break
print(lista)