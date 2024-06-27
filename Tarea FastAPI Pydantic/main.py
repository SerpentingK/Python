from fastapi import FastAPI, HTTPException
from models import *
import json

app = FastAPI()

def cargarJson(ruta, clase):
    try:
        with open(ruta, "r") as txt:
            return [clase(**j) for j in json.load(txt)]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def actualizarJson(ruta, lista):
    with open(ruta, "w") as txt:
        json.dump([j.dict() for j in lista], txt, indent=4)


def verificarID(id, l):
    for i in l:
        if i.id == id:
            return False
    return True
def añadirProductos():
    r = int(input("Cuantos productos desea ingresar?\n"))
    for i in range(r):
        print(f"Producto {i + 1}")
        x = True
        while x:
            id = input("Ingrese id: ")
            if verificarID(id, listaProductos):
                print("ID valida")
                x = False
            else:
                print("ID existente")

            
        name = input("Ingrese name: ")
        x = True
        while x:
            price = float(input("Ingrese price: "))
            if price <= 0:
                print("Precio invalido, ingrese de nuevo.")
            else:
                x = False
        x = True
        while x:
            amount = int(input("Ingrese amount: "))
            if amount <= 0:
                print("Cantidad invalida, ingrese de nuevo.")
            else:
                x = False
                
        if price * amount >= 500000:
            print("Precio total mayor a 500k, producto añadido correctamente a la base de datos")
            listaProductos.append(Product(id=id, name=name, price=price, amount=amount))
            actualizarJson(rutaProductos, listaProductos)
            
        else:
            print("Precio total menor a 500k, producto no añadido a la base de datos")

        


rutaProductos = "BDProductos.json"
rutaUsuarios = "BDUsuarios.json"
rutaOrdenes = "BDOrdenes.json"

listaProductos = cargarJson(rutaProductos, Product)
listaUsuarios = cargarJson(rutaUsuarios, User)
listaOrdenes = cargarJson(rutaOrdenes, Order)

       
actualizarJson(rutaProductos, listaProductos)
actualizarJson(rutaUsuarios, listaUsuarios)
actualizarJson(rutaOrdenes, listaOrdenes)

añadirProductos()
@app.get("/product")
async def default():
    if len(listaProductos) == 0:
        raise HTTPException(status_code=404, detail="Lista Vacia")
    else:
        return listaProductos
    
@app.get("/product/{id}")
async def search_for_id(id:str):
    for i in listaProductos:
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail="Producto no encontrado.")

@app.post("/product", response_model=Product)
async def add_product(product:Product):
    
    if verificarID(product.id, listaProductos):
        listaProductos.append(product)
    else:
        raise HTTPException(status_code=404, detail="Codigo de producto ya se encuentra en lista.")
          
    actualizarJson(rutaProductos, listaProductos)
    return product

@app.put("/product/{id}", response_model=Product)
async def update_product(id:str, product:Product):
    for i, p in enumerate(listaProductos):
        if p.id == id:
            listaProductos[i] = product
            actualizarJson(rutaProductos, listaProductos)
            return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/product/{id}")
async def delete_product(id:str):
    for i in listaProductos:
        if i.id == id:
            listaProductos.remove(i)
            actualizarJson(rutaProductos, listaProductos)
            raise HTTPException(status_code=200, detail="Producto eliminado")
        
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.get("/user")
async def default():
    if len(listaUsuarios) == 0:
        raise HTTPException(status_code=404, detail="Lista Vacia")
    else:
        return listaUsuarios
    
@app.get("/user/{id}")
async def search_for_id(id:str):
    for i in listaUsuarios:
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail="Usuario no encontrado.")

@app.post("/user", response_model=User)
async def add_user(user:User):
    
    if verificarID(user.id, listaUsuarios):
        listaUsuarios.append(user)
    else:
        raise HTTPException(status_code=404, detail="Codigo de usuario ya se encuentra en lista.")
          
    actualizarJson(rutaUsuarios, listaUsuarios)
    return user

@app.put("/user/{id}", response_model=User)
async def update_user(id:str, user:User):
    for i, p in enumerate(listaUsuarios):
        if p.id == id:
            listaUsuarios[i] = user
            actualizarJson(rutaUsuarios, listaUsuarios)
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/user/{id}")
async def delete_user(id:str):
    for i in listaUsuarios:
        if i.id == id:
            listaUsuarios.remove(i)
            actualizarJson(rutaUsuarios, listaUsuarios)
            raise HTTPException(status_code=200, detail="Usuario eliminado")
        
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.get("/order")
async def default():
    if len(listaOrdenes) == 0:
        raise HTTPException(status_code=404, detail="Lista Vacia")
    else:
        return listaOrdenes
    
@app.get("/order/{id}")
async def search_for_id(id:str):
    for i in listaOrdenes:
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail="Orden no encontrada.")
@app.get("/order/user/{id}")
async def search_for_user(id:str):
    # Verificar si el ID del usuario existe en la lista de usuarios
    if not any(user.id == id for user in listaUsuarios):
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    lista = []
    for i in listaOrdenes:
        if i.user_id == id:
            lista.append(i)
    if len(lista) > 0:
        return lista
    else:
        raise HTTPException(status_code=404, detail="Usuario sin ordenes.")
    
@app.get("/order/total/{id}")
async def search_for_user(id:str):
    # Verificar si el ID del usuario existe en la lista de usuarios
    if not any(user.id == id for user in listaUsuarios):
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    total = 0
    for i in listaOrdenes:
        if i.user_id == id:
            total += i.total
    if total > 0:
        return {f"Total gastado pór {next((user for user in listaUsuarios if user.id == id), None).name}": total}
    else:
        raise HTTPException(status_code=404, detail="Usuario sin ordenes.")
    
"""
Manera de añadir ordenes
{
  "id": "3",
  "user_id": "2",
  "product_list": ["2", "2", "1"]
}

"""

@app.post("/order", response_model=Order)
async def add_order(order: Order):
    # Verificar si el ID de la orden ya existe
    if not verificarID(order.id, listaOrdenes):
        raise HTTPException(status_code=400, detail="Código de orden ya se encuentra en la lista.")

    # Verificar si el ID del usuario existe en la lista de usuarios
    if not any(user.id == order.user_id for user in listaUsuarios):
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    # Verificar si todos los IDs de los productos existen en la lista de productos
    total = 0
    for product_id in order.product_list:
        product = next((product for product in listaProductos if product.id == product_id), None)
        if product is None:
            raise HTTPException(status_code=404, detail=f"Producto con ID {product_id} no encontrado.")
        total += product.price

    # Asignar el total calculado a la orden
    order.total = total

    # Añadir la orden a la lista de órdenes
    listaOrdenes.append(order)
    actualizarJson(rutaOrdenes, listaOrdenes)
    return order

@app.put("/order/{id}", response_model=Order)
async def update_order(id:str, order:Order):
    for i, p in enumerate(listaOrdenes):
        if p.id == id:
            listaOrdenes[i] = order
            actualizarJson(rutaOrdenes, listaOrdenes)
        return order
    raise HTTPException(status_code=404, detail="Orden no encontrado")

@app.delete("/order/{id}")
async def delete_order(id:str):
    for i in listaOrdenes:
        if i.id == id:
            listaOrdenes.remove(i)
            actualizarJson(rutaOrdenes, listaOrdenes)
            raise HTTPException(status_code=200, detail="Orden eliminada")
        
    raise HTTPException(status_code=404, detail="Orden no encontrado")
