def mayor_producto(a, b, c, d):
    productos = [a*b, a*c, a*d, b*c, b*d, c*d]
    productos_ordenados = productos.copy()
    productos_ordenados.sort()
    return productos_ordenados[-1]

# Solicitar los números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
num4 = float(input("Introduce el cuarto número: "))

resultado = mayor_producto(num1, num2, num3, num4)
print("El mayor producto de dos números es:", resultado)
