import tkinter as tk 

def saludar(): 
 nombre = entrada.get() 
 edad= entrada1.get()
 etiqueta_resultado.config(text=f"Hola {nombre} tienes {edad} años") 
 
ventana = tk.Tk() 
ventana.title("Mi primera app grafica") 
ventana.geometry("500x300") 
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:") 
etiqueta.pack() 
entrada = tk.Entry(ventana) 
entrada.pack() 
etiqueta = tk.Label(ventana, text="Ingresa tu edad:") 
etiqueta.pack() 
entrada1 = tk.Entry(ventana) 
entrada1.pack()
boton = tk.Button(ventana, text="Saludar", command=saludar) 
boton.pack() 
etiqueta_resultado = tk.Label(ventana, text="") 
etiqueta_resultado.pack() 
etiqueta = tk.Label(ventana, text="Programa realizado por toño") 
etiqueta.pack() 

ventana.mainloop()
