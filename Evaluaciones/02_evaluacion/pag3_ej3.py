# Ingresar los datos por teclado
n = int(input("Ingrese el número de productos: "))
productos = {}
for i in range(n):
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos[producto] = precio

# Función para ordenar el diccionario por precio
def ordenar_productos(productos):
    productos_ordenados = []
    while len(productos) > 0:
        producto_mas_barato = None
        for producto, precio in productos.items():
            if producto_mas_barato is None or precio < productos[producto_mas_barato]:
                producto_mas_barato = producto
        productos_ordenados.append(producto_mas_barato)
        del productos[producto_mas_barato]
    return productos_ordenados

# Llamar a la función e imprimir el resultado
productos_ordenados = ordenar_productos(productos)
print("Productos ordenados por precio de menor a mayor:")
for producto in productos_ordenados:
    print(producto)
