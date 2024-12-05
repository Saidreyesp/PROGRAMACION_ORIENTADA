class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.__contrasena = contrasena  # Atributo privado

    def verificar_contrasena(self, contrasena):
        if self.__contrasena == contrasena:
            return "Acceso concedido"
        else:
            return "Acceso denegado"

    def cambiar_contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena
        return "Contraseña actualizada"

if __name__ == "__main__":
    usuario = Usuario("Juan", "12345")
    print(usuario.verificar_contrasena("12345"))  # Acceso concedido
    print(usuario.verificar_contrasena("54321"))  # Acceso denegado
    print(usuario.cambiar_contrasena("nueva123"))
    print(usuario.verificar_contrasena("nueva123"))  # Acceso concedido
