# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Se ingresan 7 días
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal
def main():
    print("Registro de Temperaturas Semanales")
    temperaturas = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas)
    print(f"La temperatura promedio semanal es: {promedio_semanal:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()