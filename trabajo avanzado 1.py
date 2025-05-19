import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
def bienvenida():
    limpiar_ventana()
    tk.Label(area_dinamica, text="Mensaje de bienvenida:", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar bienvenida", command=lambda: messagebox.showinfo("Bienvenida", "Bienvenido")).pack()

def capturar_datos():
    limpiar_ventana()
    tk.Label(area_dinamica, text="Llena los datos para identificarte", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Sexo:").pack()
    opcion_elegida = tk.StringVar(value="Hombre")
    tk.Radiobutton(area_dinamica, text="Hombre", variable=opcion_elegida, value="Hombre").pack()
    tk.Radiobutton(area_dinamica, text="Mujer", variable=opcion_elegida, value="Mujer").pack()

    tk.Label(area_dinamica, text="Grado:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Primero", "Segundo", "Tercero"])
    combo.pack()
    combo.current(0)

    def mostrar_datos():
        valor = campo_texto_uno.get()
        a=tk.Label(area_dinamica, text=(f"Nombre: {valor}\nSexo: {opcion_elegida.get()}\nGrado: {combo.get()}")).pack()

    tk.Button(area_dinamica, text="Mostrar", command=mostrar_datos).pack(pady=10)

def cambiar_color():
    limpiar_ventana()
    tk.Label(area_dinamica, text="Personalizacion temporal", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def ayuda():
    limpiar_ventana()
    tk.Label(area_dinamica, text="Texto de ayuda que el alumno debe mejorar", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def limpiar_ventana():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Bienvenida", command=bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Capturar datos", command=capturar_datos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Personalizar el color", command=cambiar_color, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda al alumno", command=ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)
bienvenida()
ventana_principal.mainloop()