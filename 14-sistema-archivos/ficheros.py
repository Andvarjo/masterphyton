from io import open
import pathlib
import shutil
#abrir archivo

#archivo=open("14-sistema-archivos/fichero_texto.txt","a+")

ruta=str(pathlib.Path().absolute())+ "/fichero_texto.txt" #mejor manera de abrir
archivo=open(ruta,"a+")

#escribir

archivo.write("*****soy un texto metido desde python****\n")
archivo=open(ruta,"a+")

#cerrar archivo

archivo.close()

#abrir archivo y leer de el

ruta=str(pathlib.Path().absolute())+ "/fichero_texto.txt" #mejor manera de abrir
archivo_lectura=open(ruta,"r") #r para leer

#contenido=archivo_lectura.read()
#print(contenido)

#leer contenido y guardarlo en lista

lista=archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print("-"+frase.upper())

'''
#####copiar un archivo modulo shutil

ruta_original=str(pathlib.Path().absolute())+ "/fichero_texto.txt" 
ruta_nueva=str(pathlib.Path().absolute())+ "/fichero_copiado.txt" 
ruta_alternativa=str(pathlib.Path().absolute())+"/07-ejercicios/fichero_copiado77.txt" 

shutil.copyfile(ruta_original,ruta_nueva)
shutil.copyfile(ruta_original,ruta_alternativa)


#mover archivo

ruta_original=str(pathlib.Path().absolute())+ "/fichero_copiado.txt" 
ruta_nueva=str(pathlib.Path().absolute())+ "/fichero_copiado_nuevo.txt" 
shutil.move(ruta_original,ruta_nueva)
'''
#eliminar con modulo os

import os
'''
ruta_nueva=str(pathlib.Path().absolute())+ "/fichero_copiado_nuevo.txt" 

os.remove(ruta_nueva)
'''
#comprobar si archivo existe

import os.path

ruta_comprobar=os.path.abspath("./")+"/fichero_texto.txt"


if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print("el archivo no existe")