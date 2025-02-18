import os
import json


class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - ${self.precio:.2f} - {self.cantidad} unidades"


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo si existe."""
        try:
            if os.path.exists(self.ARCHIVO_INVENTARIO):
                with open(self.ARCHIVO_INVENTARIO, "r", encoding="utf-8") as file:
                    datos = file.read()
                    if datos:
                        self.productos = json.loads(datos)
                        print("Inventario cargado correctamente.")
            else:
                print("No se encontró un archivo de inventario. Se creará uno nuevo al guardar datos.")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error al cargar el inventario: {e}")
        except PermissionError:
            print("No se tienen permisos para leer el archivo de inventario.")

    def guardar_inventario(self):
        """Guarda los productos en el archivo."""
        try:
            with open(self.ARCHIVO_INVENTARIO, "w", encoding="utf-8") as file:
                json.dump(self.productos, file, indent=4)
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("No se tienen permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print("Error: El producto ya existe en el inventario.")
        else:
            self.productos[producto.codigo] = vars(producto)
            self.guardar_inventario()
            print("Producto agregado correctamente.")

    def actualizar_producto(self, codigo, precio=None, cantidad=None):
        if codigo in self.productos:
            if precio is not None:
                self.productos[codigo]['precio'] = precio
            if cantidad is not None:
                self.productos[codigo]['cantidad'] = cantidad
            self.guardar_inventario()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, codigo):
        return self.productos.get(codigo, "Producto no encontrado")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(
                    f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']:.2f} - {producto['cantidad']} unidades")
        else:
            print("El inventario está vacío.")


# Interfaz en consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(Producto(codigo, nombre, precio, cantidad))
        elif opcion == "2":
            codigo = input("Código del producto a actualizar: ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = float(precio) if precio else None
            cantidad = int(cantidad) if cantidad else None
            inventario.actualizar_producto(codigo, precio, cantidad)
        elif opcion == "3":
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "4":
            codigo = input("Código del producto a buscar: ")
            print(inventario.buscar_producto(codigo))
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventarios.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
