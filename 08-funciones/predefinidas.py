nombre="Andres Varela"

#funciones generales
print(nombre)
print(type(nombre))

#detectar el tipado

comprobar=isinstance(nombre,int) #isinstance comprueba el tipo de dato
if comprobar:
    print("esa vasriable es un string")
else:
    print("esa variable no es una cadena")
    
# limpiar espacios de un string

frase="    mi contenido  "
print(frase)
print(frase.strip())  #quita los espacios

#eliminar variables

year=2022
print(year)
del year          #del borra la variable
#print(year)


#comprobar variable vacia

texto="   ff   "

if len(texto)<=0:
    print("la variable esta vacia")
else:
    print("la variable tiene contenido",len(texto))
    
#encontrar caracteres

frase="la vida es bella"

print(frase.find("vida"))  #me devuelve a partir de que posicion se encuentra

#reemplazar palabras en un string

nueva_frase=frase.replace("vida","moto")
print(nueva_frase)

#mayusculas y minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())
