# Ejercicio 33: Operaciones matemáticas con dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 == num2:
    resultado = num1 * num2
elif num1 > num2:
    resultado = num1 - num2
else:
    resultado = num1 + num2

print(f"El resultado es: {resultado}")
