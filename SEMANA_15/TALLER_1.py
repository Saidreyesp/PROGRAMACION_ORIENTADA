import tkinter as tk
from tkinter import messagebox


class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Frame para la entrada de tareas
        self.task_entry_frame = tk.Frame(root)
        self.task_entry_frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(self.task_entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", self.add_task)  # Añadir tarea con Enter

        # Botón para añadir tarea
        self.add_button = tk.Button(self.task_entry_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Frame para los botones de acciones
        self.action_buttons_frame = tk.Frame(root)
        self.action_buttons_frame.pack(pady=10)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.action_buttons_frame, text="Marcar como Completada",
                                         command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.action_buttons_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)

    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea válida.")

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"✓ {task}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
