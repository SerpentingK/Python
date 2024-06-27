from clases import Libro

libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico"),
    Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasía"),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela"),
]

Libro.buscar_por_autor(libros, "Gabriel García Márquez")
Libro.buscar_por_genero(libros, "Fantasía")

libros[0].prestar()
libros[0].prestar()
libros[0].devolver()
libros[0].devolver()