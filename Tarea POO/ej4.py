from clases import Producto

producto_1 = Producto("Camiseta", 20, 50)
producto_2 = Producto("Pantalón", 30, 30)

print(producto_1)
print(producto_2)

producto_1.actualizar_stock(10)

print("Nuevo stock de camisetas:", producto_1.cantidad)

valor_total_inventario = producto_1.calcular_valor_inventario() + producto_2.calcular_valor_inventario()
print("Valor total del inventario:", valor_total_inventario)
