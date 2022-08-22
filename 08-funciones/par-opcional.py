#### parametros opcionales

def getEmpleado(nombre,ID = None):  #le asigno un valor al segundo parametro
    print("Empleado")
    print(f"nombre: {nombre}")
    if ID !=None:
        print(f"ID: {ID}")



print("---------con dos parametros")
print("\n")
getEmpleado("andres varela",1144052365)  #se asigan los dos parametros
print("\n")
print("---------con un parametro")
print("\n")
getEmpleado("andres varela") #no asigno el segundo aprametro y no lo imprime
print("\n")