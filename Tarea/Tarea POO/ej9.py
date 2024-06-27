from clases import Paquete


paquete_1 = Paquete("123456789", "Ciudad A", "Ciudad B")
print(paquete_1.consultar_ubicacion())

paquete_1.actualizar_estado("En almacén")
print(paquete_1.consultar_ubicacion())
