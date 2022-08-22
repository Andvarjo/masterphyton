from tkinter import *

ventana=Tk()

#ventana.geometry('700x500')

texto=Label(ventana,text="Bienvenido a mi programa")
texto.config(
    
    fg="white",
    bg="#000000", #000000 corresponde a black
    padx=50,
    pady=20,
    font=("Arial",30)
    
    
    )
texto.pack(side=TOP)
texto=Label(ventana,text="Soy Andres Varela")
texto.config(
    height=3,
    bg='orange',
    font=("Arial",18),
    padx=10,
    pady=10,
    cursor="spider"   
)
texto.pack(side=TOP,fill=X,expand=YES) # con la opcion anchor se ubican los elemntos dentro de la ventana


texto=Label(ventana,text='basico 1')
texto.config(
    height=3,
    bg='green',
    font=("Arial",18),
    padx=10,
    pady=10,
    cursor="spider"   
)
texto.pack(side=LEFT,fill=X,expand=YES) # con la opcion anchor se ubican los elemntos dentro de la ventana

texto=Label(ventana,text='basico 2')
texto.config(
    height=3,
    bg='purple',
    font=("Arial",18),
    padx=10,
    pady=10,
    cursor="spider"   
)
texto.pack(side=LEFT,fill=X,expand=YES) 

texto=Label(ventana,text='basico 3')
texto.config(
    height=3,
    bg='blue',
    font=("Arial",18),
    padx=10,
    pady=10,
    cursor="spider"   
)
texto.pack(side=LEFT,fill=X,expand=YES) 
ventana.mainloop()

