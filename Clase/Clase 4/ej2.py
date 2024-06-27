'''
    Hacer un algoritmo que le pida al usuario x cantidad de productos de los que ingresara nombre y valor. Despues se debe poder reazliar una venta de producto donde el cliente pide un producto por el nombre, cantidad y el algorimto debe decir cuanto debe pagar.  
'''

productos = []
precios = []
compras = []
precioCompras = []
cantidades = []
y = True
def agregarProducto():
    global y
    pro = input('Ingrese nombre de producto:')
    if(pro != "-1"):
        pre = int(input("Ingrese precio del producto: $"))
        productos.append(pro.capitalize())
        precios.append(pre)
    elif pro == "-1":
        y = False
    
    
def pedirProducto(indice, cantidad):
    compras.append(productos[indice])
    precioCompras.append(precios[indice] * cantidad)
    cantidades.append(cantidad)

def mostrarCompras():
    print("---Compras---")
    for i in range(len(compras)):
        print(f"{compras[i]}: ${precioCompras[i]} // Cantidad: {cantidades[i]}")
    total = 0
    for i in precioCompras:
        total += i
    print(f"Total: {total}")

while y:
    print("---Ingreso de productos---")
    agregarProducto()
    
y = True
while y:
    print("---Compra de productos---")
    for i in range(len(productos)):
        print(f"{productos[i]}: ${precios[i]}")
    x = True
    while x:
        pedido = input("Ingrese el producto que desea comprar (-1 para salir): ").capitalize()
        if pedido in productos:
            x = False
        elif pedido == "-1":
            y = False
        else:
            print("Producto no se encuentra en lista")
    x = True
    while x:
        cantidad = int(input("Cantidad: "))
        if cantidad > 0:
            pedirProducto(productos.index(pedido), cantidad)
            x = False
        else:
            print("Cantidad invalida")
    
mostrarCompras()
    
