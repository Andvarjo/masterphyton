import os,shutil

#crear carpeta

if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):
    os.mkdir("./14-sistema-archivos/mi_carpeta")
else:
    print("ya existe eld irectorio")

'''   
##############elimiar

os.rmdir("./14-sistema-archivos/mi_carpeta")


#########copiar carpeta

ruta_original="./14-sistema-archivos/mi_carpeta"
ruta_nueva="./14-sistema-archivos/mi_carpeta_copiada"
shutil.copytree(ruta_original,ruta_nueva)

'''
print("contenido de mi carpeta")

contenido=os.listdir("./14-sistema-archivos/mi_carpeta")

for fichero in contenido:
    print("ficehro: "+fichero)