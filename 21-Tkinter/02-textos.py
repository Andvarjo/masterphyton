from tkinter import *

ventana=Tk()

ventana.geometry('700x500')

texto=Label(ventana,text="Bienvenido a mi programa")
texto.config(
    
    fg="white",
    bg="#000000", #000000 corresponde a black
    padx=50,
    pady=20,
    font=("Arial",30)
    
    
    )
texto.pack()
texto=Label(ventana,text="Soy Andres Varela")
texto.config(
    height=3,
    bg='orange',
    font=("Arial",18),
    padx=10,
    pady=10,
    cursor="spider"   
)
texto.pack(anchor=SE) # con la opcion anchor se ubican los elemntos dentro de la ventana

def pruebas(nombre,apellidos,pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto=Label(ventana,text=pruebas(pais="Colombia",nombre="andres",apellidos="varela"))
texto.config(
    height=3,
    bg='green',
    font=("Arial",18),
    padx=10,
    pady=10,
    cursor="spider"   
)
texto.pack(anchor=NW) # con la opcion anchor se ubican los elemntos dentro de la ventana

ventana.mainloop()

