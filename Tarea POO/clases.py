class Calculadora:
    def __init__(self):
        print("Se ha creado la calculadora")
        
    def suma(self, n1, n2):
        return n1 + n2
    def resta(self, n1, n2):
        return n1 - n2
    def multiplicacion(self, n1, n2):
        return n1 * n2
    def division(self, n1,n2):
        return n1 * n2
    
class Cuenta:
    saldo = float()
    
    def getSaldo(self):
        return(self.saldo)
    
    def deposito(self, deposito):
        self.saldo += deposito
    def retiro(self, retiro):
        if retiro > self.saldo:
            print("Retiro invalido")
        else:
            self.saldo -= retiro
            
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre}: Precio ${self.precio}, Stock {self.cantidad}"

    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad

    def calcular_valor_inventario(self):
        return self.precio * self.cantidad

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - Estado: {estado}"

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True

    def listar_tareas_pendientes(self):
        tareas_pendientes = [tarea for tarea in self.tareas if not tarea.completada]
        if tareas_pendientes:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas_pendientes, start=1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas pendientes.")
class Vuelo:
    def __init__(self, origen, destino, asientos_disponibles):
        self.origen = origen
        self.destino = destino
        self.asientos_disponibles = asientos_disponibles

    def reservar_asientos(self, cantidad):
        if cantidad <= self.asientos_disponibles:
            self.asientos_disponibles -= cantidad
            print(f"Reserva realizada para {cantidad} asientos.")
        else:
            print("No hay suficientes asientos disponibles.")

    def consultar_disponibilidad(self):
        print(f"Asientos disponibles: {self.asientos_disponibles}")

class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print("Libro prestado.")
        else:
            print("El libro ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print("Libro devuelto.")
        else:
            print("El libro no estaba prestado.")

    @staticmethod
    def buscar_por_autor(libros, autor):
        libros_encontrados = [libro for libro in libros if libro.autor == autor]
        if libros_encontrados:
            print(f"Libros encontrados del autor {autor}:")
            for libro in libros_encontrados:
                print(f"- {libro.titulo}")
        else:
            print(f"No se encontraron libros del autor {autor}.")

    @staticmethod
    def buscar_por_genero(libros, genero):
        libros_encontrados = [libro for libro in libros if libro.genero == genero]
        if libros_encontrados:
            print(f"Libros encontrados del género {genero}:")
            for libro in libros_encontrados:
                print(f"- {libro.titulo}")
        else:
            print(f"No se encontraron libros del género {genero}.")
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad=1):
        self.productos.append({"producto": producto, "cantidad": cantidad})

    def calcular_total(self):
        total = sum(item["producto"].precio * item["cantidad"] for item in self.productos)
        return total

    def realizar_pago(self, monto):
        total = self.calcular_total()
        if monto < total:
            print("El monto ingresado es insuficiente.")
            return False
        else:
            cambio = monto - total
            print(f"Pago realizado correctamente. Su cambio es de ${cambio:.2f}.")
            self.productos = []
            return True
class Paquete:
    def __init__(self, numero_seguimiento, origen, destino, estado_actual="En tránsito"):
        self.numero_seguimiento = numero_seguimiento
        self.origen = origen
        self.destino = destino
        self.estado_actual = estado_actual

    def actualizar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado

    def consultar_ubicacion(self):
        return f"El paquete se encuentra en {self.estado_actual}"
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"

class GestorContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto {contacto.nombre} agregado.")

    def buscar_contacto(self, nombre):
        contactos_encontrados = [contacto for contacto in self.contactos if contacto.nombre == nombre]
        if contactos_encontrados:
            print(f"Contactos encontrados con el nombre '{nombre}':")
            for contacto in contactos_encontrados:
                print(contacto)
        else:
            print(f"No se encontraron contactos con el nombre '{nombre}'.")

    def eliminar_contacto(self, nombre):
        self.contactos = [contacto for contacto in self.contactos if contacto.nombre != nombre]
        print(f"Contacto(s) con el nombre '{nombre}' eliminado(s).")
class Estudiante:
    
    nombre = str()
    edad = int()
    calificaciones = list()
    
    def __init__(self, nombre, edad, calif):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calif

    # Setter y Getter para nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    # Setter y Getter para edad
    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    # Setter y Getter para calificaciones
    def add_calificaciones(self, calificacion):
        self.calificaciones.append(calificacion)

    def get_calificaciones(self):
        return self.calificaciones
    
    def cal_promedio(self):
        total = 0
        for i in self.calificaciones:
            total += i
        promedio = total/len(self.calificaciones)   
        return promedio

