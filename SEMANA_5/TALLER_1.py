# Programa para convertir temperaturas entre Celsius y Fahrenheit
# Funcionalidad: Este programa permite al usuario convertir una temperatura de Celsius a Fahrenheit y viceversa.

def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte una temperatura de Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

# Menú para que el usuario elija la conversión
print("Conversión de temperaturas:")
print("1. Convertir de Celsius a Fahrenheit")
print("2. Convertir de Fahrenheit a Celsius")

opcion = int(input("Elige una opción (1 o 2): "))

if opcion == 1:
    celsius = float(input("Introduce la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
elif opcion == 2:
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit}°F equivalen a {celsius:.2f}°C")
else:
    print("Opción no válida. Por favor, elige 1 o 2.")
