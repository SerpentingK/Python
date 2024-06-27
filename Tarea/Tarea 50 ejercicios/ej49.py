# Ejercicio 49: Calcular n términos de la serie Fibonacci

# Solicitar al usuario el número de términos
n = int(input("Ingrese el número de términos de la serie Fibonacci: "))

# Inicializar los primeros dos términos de la serie
a, b = 0, 1
print(a, end=" ")
print(b, end=" ")

# Calcular los siguientes términos de la serie y mostrarlos
for _ in range(n - 2):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

print()  # Salto de línea al final
