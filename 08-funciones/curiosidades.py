
def mi_funcion(nombre):
    return "hola que tal" + nombre
    
def mi_funcion2(apellido):
    return "hola que tal 2 " + apellido
#lo mas recomendable es declarar las funciones al inicio
# es mas recomendable hacer los print por fuera de la funcion y retornar valores

nombre="Andres"
apellido="Varela"

print("hola mundo")

print(f"bienvenido {nombre}")
# definir las variable santes de llamarlas
print (mi_funcion(nombre))
print(mi_funcion2(apellido))

