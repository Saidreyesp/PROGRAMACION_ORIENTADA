class CarritoCompras:
    def __init__(self):
        """
        Constructor que inicializa el carrito como una lista vacía.
        """
        self.items = []
        print("Carrito de compras creado. ¡Listo para agregar productos!")

    def agregar_producto(self, producto):
        """
        Agrega un producto al carrito.
        :param producto: Nombre del producto a agregar.
        """
        self.items.append(producto)
        print(f"Producto '{producto}' agregado al carrito.")

    def mostrar_carrito(self):
        """
        Muestra todos los productos en el carrito.
        """
        if self.items:
            print("Productos en el carrito:")
            for producto in self.items:
                print(f"- {producto}")
        else:
            print("El carrito está vacío.")

    def __del__(self):
        """
        Destructor que vacía el carrito antes de eliminar el objeto.
        """
        print("Vaciando el carrito de compras...")
        self.items.clear()
        print("Carrito eliminado correctamente. ¡Gracias por comprar!")

# Uso de la clase
carrito = CarritoCompras()
carrito.agregar_producto("Laptop")
carrito.agregar_producto("Mouse")
carrito.mostrar_carrito()

# Al finalizar el programa o eliminar el objeto, el destructor vaciará el carrito.
del carrito
