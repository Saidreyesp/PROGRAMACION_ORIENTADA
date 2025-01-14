# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Vehículo marca {self.marca}, modelo {self.modelo}."


# Clase derivada
class Auto(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.__kilometraje = 0  # Atributo encapsulado
        self.num_puertas = num_puertas

    def descripcion(self):  # Polimorfismo
        return f"Auto marca {self.marca}, modelo {self.modelo}, con {self.num_puertas} puertas."

    # Métodos getter y setter
    def get_kilometraje(self):
        return self.__kilometraje

    def set_kilometraje(self, kilometraje):
        if kilometraje >= 0:
            self.__kilometraje = kilometraje
        else:
            print("El kilometraje no puede ser negativo.")

    def encender(self):
        return "El auto está encendido."


# Ejemplo de uso
if __name__ == "__main__":
    auto = Auto("Toyota", "Corolla", 4)
    print(auto.descripcion())
    auto.set_kilometraje(13000)
    print(f"Kilometraje: {auto.get_kilometraje()} km")
    print(auto.encender())
