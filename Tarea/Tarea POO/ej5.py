from clases import GestorTareas

gestor = GestorTareas()
gestor.agregar_tarea("Comprar leche")
gestor.agregar_tarea("Hacer ejercicio")
gestor.agregar_tarea("Estudiar para el examen")

gestor.marcar_completada(1)

gestor.listar_tareas_pendientes()