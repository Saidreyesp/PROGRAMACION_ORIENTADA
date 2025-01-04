class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" no está disponible.')

    def devolver(self):
        self.disponible = True
        print(f'El libro "{self.titulo}" ha sido devuelto.')

# Ejemplo de uso
libro1 = Libro("Un Mapa En La Cabeza", "Ken jenning", "123456789")
libro1.prestar()
libro1.devolver()
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro "{self.titulo}" ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" no está disponible.')

    def devolver(self):
        self.disponible = True
        print(f'El libro "{self.titulo}" no ha sido devuelto.')

# Ejemplo de uso
libro1 = Libro("Una vida extraordinaria", "Juan Benigno", "123456789")
libro1.prestar()
libro1.devolver()
