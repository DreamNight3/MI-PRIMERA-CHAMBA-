import tkinter as tk
from tkinter import messagebox
def mostrar_mensaje():
  nomb= nombre.get()
  messagebox.showinfo("Mensaje", f"Hola{nomb}bienvenido al programa")
#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI ")
#Crear una etiqueta
etiqueta = tk.Label(ventana, text="Ingresa tu nombre: ")
etiqueta.grid(row=0, column=0, padx=5, pady=10)
#Crea una caja de texto (Entry)
nombre = tk.Entry(ventana, width=40)
nombre.grid(row=0, column=1, padx=5, pady=10)
#Crea un boton y asignarle a la funcion
boton = tk.Button(ventana, text="saludar", command=mostrar_mensaje)
boton.grid(row=1, column=0, columnspan=2, pady=10)
#Iniciar el bucle de eventos
ventana.mainloop()