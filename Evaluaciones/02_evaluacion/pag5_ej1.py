def suma_digitos_y_cuenta(num):
    suma_digitos = 0
    while num > 0:
        suma_digitos += num % 10
        num //= 10

    cuenta_digitos = 0
    while suma_digitos > 0:
        cuenta_digitos += 1
        suma_digitos //= 10

    return cuenta_digitos

# Ingreso de datos
numero = int(input("Ingrese un número: "))

# Llamada a la función e impresión del resultado
resultado = suma_digitos_y_cuenta(numero)
print(resultado)
