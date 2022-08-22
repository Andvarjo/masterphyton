from tkinter import *
from PIL import Image, ImageTk

ventana=Tk()
ventana.geometry("700x500")

Label(ventana,text="hola soy andres").pack(anchor=W)

imagen=Image.open('./21-Tkinter/imagenes/megaman.jpg')
render=ImageTk.PhotoImage(imagen)
Label(ventana,image=render).pack(anchor=SE)


ventana.mainloop()