"""  
Tkinter es un modulo para crear interfaces graficas
de usuario
"""
from cgitb import text
from tkinter import*
import os.path


class Programa:
   
   def __init__(self):
      
      self.title="Master en python con NAdres Varela"
      self.icon="./imagenes/gameboy.ico"
      self.icon_alt="./21-Tkinter/imagenes/gameboy.ico"
      self.size="740x470"
      self.resizable=False
   
   def cargar(self):
      

      #comprobar is existe un archivo

      ruta_icono=os.path.abspath(self.icon)

      if not os.path.isfile(ruta_icono):
         ruta_icono=os.path.abspath(self.icon_alt)



      #crear ventana raiz

      ventana=Tk()
      self.ventana=ventana
      #mostar texto en el programa

      texto=Label(ventana, text=ruta_icono)
      texto.pack()

      #titulo de la ventana

      ventana.title(self.title)

      # icono de la ventana

      ventana.iconbitmap(ruta_icono)

      # cambio en el tamano de la ventana

      ventana.geometry(self.size)

      #bloquear el tamano de la ventana

      if self.resizable:
         ventana.resizable(1,1) #primer parametro es ancho y el segundo el alto (1=deja cambiar)
      else:
         ventana.resizable(0,0)

     
   
   
   def addTexto(self,dato):
      texto=Label(self.ventana,text=dato)
      texto.pack()  
   
   
   def mostrar(self):
      # arrancar y mostar la ventana hasta que se cierre
      self.ventana.mainloop()
      
      
      
# INSTANCIAR EL OBJETO

programa=Programa()
programa.cargar()
programa.addTexto("Hola soy un texto desde funcion")
programa.mostrar()