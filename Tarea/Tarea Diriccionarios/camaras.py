
#funciones basicas
def sumar(num1, num2):
    return num1 + num2

a = 1
b = 2

c = sumar(a, b)
print(c)

d = 3 + sumar(a, b)
print(d)

#funciones2

lista = ["Juan", 15, 1.75]

def modif_edad(lista, nuevaEdad):
    nuevaLista = lista.copy()
    nuevaLista[1] = nuevaEdad
    return nuevaLista

lista = modif_edad(lista, 20)
print(lista)

#ejercico Juli 1
num1=int(input("ingrese el primer numero "))
num2=int(input("ingrese el primer numero "))

def dividir(num1, mum2):
    return num1/num2
division= dividir(num1,num2)

print(division)

#ejercicio Juli 2
'''funcion recibe una lista y devuelve los numeros pares'''
lista=[1,2,3,4,5,6,7,8,9,10]
def pares(lista):
    nuevalista=list()
    for i in lista:
        if i % 2 == 0:
            nuevalista.append(i)
    return nuevalista
pares=pares(lista)
print(pares)
