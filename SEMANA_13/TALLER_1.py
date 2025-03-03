import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()  # Obtener el dato del campo de texto
    if dato:  # Verificar que el campo no esté vacío
        lista.insert(tk.END, dato)  # Agregar el dato a la lista
        entrada.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Borrar todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")

# Crear y posicionar los componentes
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.grid(row=0, column=0, padx=10, pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.grid(row=0, column=1, padx=10, pady=10)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.grid(row=0, column=2, padx=10, pady=10)

lista = tk.Listbox(ventana, width=40, height=10)
lista.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.grid(row=2, column=1, padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
