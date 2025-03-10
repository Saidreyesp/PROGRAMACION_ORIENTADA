import tkinter as tk
from tkinter import ttk, messagebox

class AgendaPersonal:
    def __init__(self, root):  # Corregido _init_ a __init__
        self.root = root
        self.root.title("Agenda Personal")
        self.eventos = []

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root)
        self.frame_lista.pack(pady=10)

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(root)
        self.frame_entrada.pack(pady=10)

        # Campos de entrada y etiquetas
        ttk.Label(self.frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = ttk.Entry(self.frame_entrada)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(pady=10)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).pack(side=tk.LEFT, padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.eventos.append((fecha, hora, descripcion))
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.fecha_entry.delete(0, tk.END)
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son requeridos")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            item = self.tree.item(seleccionado)
            evento = item['values']
            confirmacion = messagebox.askyesno("Confirmar", f"¿Eliminar el evento: {evento[2]}?")
            if confirmacion:
                self.tree.delete(seleccionado)
                self.eventos = [evt for evt in self.eventos if evt != evento]
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

if __name__ == "__main__":  # _name_ a __name__ y _main_ a "__main__"
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
