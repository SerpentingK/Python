# Ejercicio 47: Determinar el número medio de tres números diferentes

# Leer los tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Determinar el número medio
if num1 > num2:
    if num1 < num3:
        numero_medio = num1
    elif num2 > num3:
        numero_medio = num2
    else:
        numero_medio = num3
else:
    if num1 > num3:
        numero_medio = num1
    elif num2 < num3:
        numero_medio = num2
    else:
        numero_medio = num3

print(f"El número medio de los tres números es: {numero_medio}")
