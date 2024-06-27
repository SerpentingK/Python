# Ejercicio 34: Encontrar el número medio de tres números diferentes
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num2 < num1 < num3 or num2 > num1 > num3:
    numero_medio = num1
elif num1 < num2 < num3 or num1 > num2 > num3:
    numero_medio = num2
else:
    numero_medio = num3

print(f"El número medio es: {numero_medio}")
