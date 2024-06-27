from clases import GestorContactos, Contacto

gestor = GestorContactos()

contacto_1 = Contacto("Juan", "123456789", "juan@example.com")
contacto_2 = Contacto("María", "987654321", "maria@example.com")

gestor.agregar_contacto(contacto_1)
gestor.agregar_contacto(contacto_2)

gestor.buscar_contacto("Juan")

gestor.eliminar_contacto("Juan")

gestor.buscar_contacto("Juan")
