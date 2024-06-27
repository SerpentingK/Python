from clases import Producto, Carrito


producto_1 = Producto("Camiseta", 20)
producto_2 = Producto("Pantalón", 30)

carrito = Carrito()
carrito.agregar_producto(producto_1)
carrito.agregar_producto(producto_2, cantidad=2)

print("Productos en el carrito:")
for item in carrito.productos:
    print(f"- {item['producto'].nombre}: ${item['producto'].precio} x {item['cantidad']}")

total = carrito.calcular_total()
print(f"Total a pagar: ${total:.2f}")

pago = 80
carrito.realizar_pago(pago)

