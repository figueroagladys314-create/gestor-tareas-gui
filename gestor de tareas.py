import tkinter as tk

# Lista para almacenar tareas
tareas = []

# ---------------- FUNCIONES ----------------

def agregar_tarea(event=None):
    texto = entrada.get()
    if texto != "":
        tareas.append({"texto": texto, "completada": False})
        actualizar_lista()
        entrada.delete(0, tk.END)

def completar_tarea(event=None):
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = True
        actualizar_lista()

def eliminar_tarea(event=None):
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        actualizar_lista()

def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        if tarea["completada"]:
            lista.insert(tk.END, "✔ " + tarea["texto"])
        else:
            lista.insert(tk.END, "✗ " + tarea["texto"])

def cerrar_app(event=None):
    ventana.quit()

# ---------------- INTERFAZ ----------------

ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# ---------------- EVENTOS DE TECLADO ----------------

ventana.bind("<Return>", agregar_tarea)      # Enter = agregar
ventana.bind("c", completar_tarea)          # C = completar
ventana.bind("d", eliminar_tarea)           # D = eliminar
ventana.bind("<Delete>", eliminar_tarea)    # Delete = eliminar
ventana.bind("<Escape>", cerrar_app)        # Escape = salir

# Ejecutar app
ventana.mainloop()