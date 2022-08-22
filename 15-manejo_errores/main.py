#capturar excepciones y manejar errores en codigo
#suceptible al fallo

try:
    nombre=input("cual es tu nombre? ")

    if len(nombre)>1:
        nombre_usuario="el nombre es :"+ nombre
    print(nombre_usuario)

except:
    print("ha ocurrido un error, introduce bien el nombre")
    
else:
    print("todo ha funcionado correctamente")

finally:
    print("fin de la iteracion")
