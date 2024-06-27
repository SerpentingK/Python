import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Inicialización de Firebase Admin SDK
cred = credentials.Certificate('ej3/t2ej3-48597-firebase-adminsdk-cxshy-34a938a683.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Definición de modelos con Pydantic
class Cliente(BaseModel):
    nombre: str
    id_cliente:str
    tipo_cliente: str  # 'personal' o 'corporativo'
    metodo_pago: str = None  # Solo para clientes personales
    id_vendedor: str = None  # Solo para clientes corporativos

class Pedido(BaseModel):
    id_pedido: str
    id_cliente: str
    fecha_pedido: str 
    lista_lineas_pedido: list

class LineaPedido(BaseModel):
    id_pedido: str
    id_producto: str
    cantidad: int

class Vendedor(BaseModel):
    nombre: str
    id_vendedor: str
    clientes_corporativos: list  # Lista de IDs de clientes corporativos


@app.post("/clientes", response_model=Cliente)
def crear_cliente(cliente: Cliente):
    # Verificar si la ID del cliente ya existe en los atributos de los documentos
    query = db.collection('Clientes').where('id_cliente', '==', cliente.id_cliente).stream()
    cliente_existe = any(doc.id for doc in query)
    if cliente_existe:
        raise HTTPException(status_code=400, detail="ID de cliente ya existe")

    # Si es cliente corporativo, verificar si el ID del vendedor existe
    if cliente.tipo_cliente == 'corporativo':
        query_vendedor = db.collection('Vendedores').where('id_vendedor', '==', cliente.id_vendedor).stream()
        vendededor_existe = any(doc.id for doc in query_vendedor)
        if not vendededor_existe:
            raise HTTPException(status_code=400, detail="ID de vendedor no encontrado")

    # Si pasa las verificaciones, agregar el cliente a Firestore
    doc_ref = db.collection('Clientes').document()
    doc_ref.set(cliente.dict())
    return {"id_cliente": doc_ref.id, **cliente.dict()}

@app.post("/pedidos", response_model=Pedido)
def crear_pedido(pedido: Pedido):
    # Verificar si el cliente asociado al pedido existe
    query = db.collection('Clientes').where('id_cliente', '==', pedido.id_cliente).stream()
    cliente_existe = any(doc.id for doc in query)
    if not cliente_existe:
        raise HTTPException(status_code=400, detail="ID de cliente no encontrado")

    # Si pasa la verificación, agregar el pedido a Firestore
    doc_ref = db.collection('Pedidos').document()
    doc_ref.set(pedido.dict())
    for i in pedido.lista_lineas_pedido:
        doc_ref2 = db.collection('LineasPedido').document()
        doc_ref2.set(i)
    return {"id_pedido": doc_ref.id, **pedido.dict()}

@app.post("/lineaspedido", response_model=LineaPedido)
def crear_linea_pedido(linea_pedido: LineaPedido):
    # Verificar si el pedido asociado a la línea de pedido existe
    query_pedido = db.collection('Pedidos').where('id_pedido', '==', linea_pedido.id_pedido).stream()
    pedido_existe = any(doc.id for doc in query_pedido)
    if not pedido_existe:
        raise HTTPException(status_code=400, detail="ID de pedido no encontrado")

    # Si pasa la verificación, agregar la línea de pedido a Firestore
    doc_ref = db.collection('LineasPedido').document()
    doc_ref.set(linea_pedido.dict())
    return {"id_linea": doc_ref.id, **linea_pedido.dict()}

@app.post("/vendedores", response_model=Vendedor)
def crear_vendedor(vendedor: Vendedor):
    # Verificar si el vendedor ya existe en los atributos de los documentos
    query = db.collection('Vendedores').where('id_vendedor', '==', vendedor.id_vendedor).stream()
    vendedor_existe = any(doc.id for doc in query)
    if vendedor_existe:
        raise HTTPException(status_code=400, detail="ID de vendedor ya existe")

    # Si pasa la verificación, agregar el vendedor a Firestore
    doc_ref = db.collection('Vendedores').document()
    doc_ref.set(vendedor.dict())
    return {"id_vendedor": doc_ref.id, **vendedor.dict()}

@app.get("/clientes")
def listar_clientes():
    clientes = db.collection('Clientes').get()
    return [{cliente.id: cliente.to_dict()} for cliente in clientes]

@app.get("/clientes/{id_cliente}")
def obtener_cliente_por_id(id_cliente: str):
    # Realiza una consulta a la colección 'Clientes' buscando un documento que tenga un atributo 'id_cliente' igual al parámetro recibido
    query = db.collection('Clientes').where('id_cliente', '==', id_cliente).limit(1)    
    results = query.stream()

    # Verifica si se encontró algún cliente que coincida con el 'id_cliente'
    for result in results:
        return {result.id: result.to_dict()}

    # Si no se encontró ningún cliente, devuelve un error 404
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.get("/pedidos")
def listar_pedidos():
    pedidos = db.collection('Pedidos').get()
    return [{pedido.id: pedido.to_dict()} for pedido in pedidos]

@app.get("/pedidos/{id_pedido}")
def obtener_pedido(id_pedido: str):
    query = db.collection('Pedidos').where('id_cliente', '==', id_pedido).limit(1)
    results = query.stream()
    
    for result in results:
        return {result.id: result.to_dict()}

    # Si no se encontró ningún cliente, devuelve un error 404
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.get("/lineaspedido")
def listar_lineas_pedido():
    lineas_pedido = db.collection('LineasPedido').get()
    return [{linea.id: linea.to_dict()} for linea in lineas_pedido]

@app.get("/lineaspedido/{id_linea}")
def obtener_linea_pedido(id_linea: str):
    linea_pedido = db.collection('LineasPedido').document(id_linea).get()
    if linea_pedido.exists:
        return {linea_pedido.id: linea_pedido.to_dict()}
    else:
        raise HTTPException(status_code=404, detail="Línea de pedido no encontrada")

@app.get("/vendedores")
def listar_vendedores():
    vendedores = db.collection('Vendedores').get()
    return [{vendedor.id: vendedor.to_dict()} for vendedor in vendedores]

@app.get("/vendedores/{id_vendedor}")
def obtener_vendedor(id_vendedor: str):
    vendedor = db.collection('Vendedores').document(id_vendedor).get()
    if vendedor.exists:
        return {vendedor.id: vendedor.to_dict()}
    else:
        raise HTTPException(status_code=404, detail="Vendedor no encontrado")
