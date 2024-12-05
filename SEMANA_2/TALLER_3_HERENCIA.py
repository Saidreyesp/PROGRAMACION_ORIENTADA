class Transporte:
    def __init__(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def descripcion(self):
        return f"Transporte con velocidad máxima de {self.velocidad_maxima} km/h."

class Coche(Transporte):
    def __init__(self, velocidad_maxima, combustible):
        super().__init__(velocidad_maxima)
        self.combustible = combustible

    def descripcion(self):
        return f"Coche con velocidad máxima de {self.velocidad_maxima} km/h y usa {self.combustible}."

class Bicicleta(Transporte):
    def __init__(self, velocidad_maxima, tipo):
        super().__init__(velocidad_maxima)
        self.tipo = tipo

    def descripcion(self):
        return f"Bicicleta {self.tipo} con velocidad máxima de {self.velocidad_maxima} km/h."

if __name__ == "__main__":
    coche = Coche(180, "gasolina")
    bicicleta = Bicicleta(27, "de montaña")
    print(coche.descripcion())
    print(bicicleta.descripcion())
