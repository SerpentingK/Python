def encontrar_producto_mas_caro():
    cantidad = int(input("Ingrese la cantidad de productos: "))
    productos = {}
    
    for i in range(cantidad):
        producto = input(f"Ingrese el nombre del producto {i + 1}: ")
        precio = float(input(f"Ingrese el precio para {producto}: "))
        productos[producto] = precio
    
    producto_mas_caro = max(productos, key=productos.get)
    precio_mas_caro = productos[producto_mas_caro]
    
    return {producto_mas_caro: precio_mas_caro}

# Ejemplo de uso
producto_mas_caro = encontrar_producto_mas_caro()
print(producto_mas_caro)
