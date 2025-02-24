class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} por {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()
        self.prestamos = {}

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro.titulo_autor[0]}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} quitado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return
        libro = self.libros_disponibles.pop(isbn)
        self.prestamos.setdefault(id_usuario, []).append(libro)
        print(f"Libro {libro.titulo_autor[0]} prestado a usuario con ID {id_usuario}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.prestamos:
            print(f"El usuario con ID {id_usuario} no tiene libros prestados.")
            return
        for libro in self.prestamos[id_usuario]:
            if libro.isbn == isbn:
                self.libros_disponibles[isbn] = libro
                self.prestamos[id_usuario].remove(libro)
                print(f"Libro {libro.titulo_autor[0]} devuelto por usuario con ID {id_usuario}.")
                return
        print(f"El libro con ISBN {isbn} no fue prestado al usuario con ID {id_usuario}.")

    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[0] == titulo]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título {titulo}.")

    def buscar_libro_por_autor(self, autor):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.titulo_autor[1] == autor]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor {autor}.")

    def buscar_libro_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.categoria == categoria]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros en la categoría {categoria}.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.prestamos and self.prestamos[id_usuario]:
            print(f"Libros prestados al usuario con ID {id_usuario}:")
            for libro in self.prestamos[id_usuario]:
                print(libro)
        else:
            print(f"El usuario con ID {id_usuario} no tiene libros prestados.")


if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-0307474728")
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", "978-0451524935")
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "978-0156012195")

    usuario1 = Usuario("Juan Pérez", 1)
    usuario2 = Usuario("Ana Gómez", 2)

    biblioteca = Biblioteca()

    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    biblioteca.prestar_libro(1, "978-0307474728")
    biblioteca.prestar_libro(2, "978-0451524935")

    biblioteca.listar_libros_prestados(1)
    biblioteca.listar_libros_prestados(2)

    biblioteca.devolver_libro(1, "978-0307474728")
    biblioteca.devolver_libro(2, "978-0451524935")

    biblioteca.buscar_libro_por_titulo("1984")
    biblioteca.buscar_libro_por_autor("Gabriel García Márquez")
    biblioteca.buscar_libro_por_categoria("Fábula")

    biblioteca.dar_de_baja_usuario(1)
    biblioteca.dar_de_baja_usuario(2)
