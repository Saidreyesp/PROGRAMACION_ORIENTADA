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


class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir un nuevo producto asegurando que el ID sea único
    def añadir_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print(f"Error: El ID {producto.get_id_producto()} ya está en uso.")
        else:
            self.productos.append(producto)
            print(f"Producto {producto.get_nombre()} añadido correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        producto_a_eliminar = None
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                producto_a_eliminar = producto
                break
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            print(f"Producto con ID {id_producto} eliminado correctamente.")
        else:
            print(f"Error: Producto con ID {id_producto} no encontrado.")

    # Actualizar cantidad o precio de un producto por ID
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado correctamente.")
                return
        print(f"Error: Producto con ID {id_producto} no encontrado.")

    # Buscar productos por nombre (puede haber nombres similares)
    def buscar_producto(self, nombre):
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(f"ID: {producto.get_id_producto()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")
        else:
            print(f"No se encontraron productos con el nombre {nombre}.")

    # Mostrar todos los productos en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(f"ID: {producto.get_id_producto()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")


# Ejemplo de uso
producto1 = Producto(101, "LAPTOP", 10, 1200.50)
producto2 = Producto(102, "MOUSE", 50, 15.99)
producto3 = Producto(103, "TECLADO", 30, 45.75)

inventario = Inventario()
inventario.añadir_producto(producto1)
inventario.añadir_producto(producto2)
inventario.añadir_producto(producto3)

# Buscar productos por nombre
inventario.buscar_producto("LAPTOP")

# Actualizar producto
inventario.actualizar_producto(102, precio=15.99)

# Eliminar producto
inventario.eliminar_producto(1)

# Mostrar todos los productos
inventario.mostrar_productos()

