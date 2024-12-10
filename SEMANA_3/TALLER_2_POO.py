class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        """Agrega una temperatura a la lista."""
        self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        """Calcula el promedio de las temperaturas ingresadas."""
        if not self.temperaturas:
            return 0
        suma = sum(self.temperaturas)
        return suma / len(self.temperaturas)


def main():
    clima = ClimaDiario()

    print("Registro de Temperaturas Semanales")

    for i in range(7):  # Se ingresan 7 días
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima.ingresar_temperatura(temp)

    promedio_semanal = clima.calcular_promedio()
    print(f"La temperatura promedio semanal es: {promedio_semanal:.2f}°C")


# Ejecutar el programa
if __name__ == "__main__":
    main()