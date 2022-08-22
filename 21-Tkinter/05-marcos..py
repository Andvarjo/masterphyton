from tkinter import *

ventana=Tk()
ventana.title("Frames Master en Python")
ventana.geometry("700x700")





marco_padre1=Frame(ventana,width=250,height=250)

marco_padre1.pack(side=TOP,fill=X,expand=YES)

marco_padre2=Frame(ventana,width=250,height=250)

marco_padre2.pack(side=BOTTOM,fill=X,expand=YES)



marco=Frame(marco_padre2,width=250,height=250)
marco.config(
    bg='red',
    bd=5,
    relief=SOLID
    
)

marco.pack(side=LEFT,anchor=SW)

marco=Frame(marco_padre2,width=250,height=250)
marco.config(
    bg='blue',
    bd=5,
    relief=SOLID
    
)
marco.pack(side=RIGHT,anchor=SE)

marco=Frame(marco_padre1,width=250,height=250)
marco.config(
    bg='purple',
    bd=5,
    relief=SOLID
    
)

marco.pack(side=LEFT,anchor=SW)

marco=Frame(marco_padre1,width=250,height=250)
marco.config(
    bg='green',
    bd=5,
    relief=SOLID
    
)
marco.pack(side=RIGHT,anchor=SE)

ventana.mainloop()