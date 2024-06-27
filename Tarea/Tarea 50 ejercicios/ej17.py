# Ejercicio 17: Leer dos números y mostrarlos en forma ascendente
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Ordenamos los números de forma ascendente
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Los números en forma ascendente son: {numero1}, {numero2}")
