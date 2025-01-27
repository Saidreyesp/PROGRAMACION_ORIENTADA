class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

# Ejemplo de uso
producto1 = Producto(101, "LAPTOP", 10, 1200.50)
print(f"Producto: {producto1.get_nombre()}, Cantidad: {producto1.get_cantidad()}, Precio: ${producto1.get_precio()}")
