#excepciones personalizadas o lanzar excepcion

try:
    nombre=input("introduce tu nombre: ")
    edad=int(input("introduce tu edad: "))

    if edad <5 or edad >110:
        raise ValueError (" La edad introducida no es real")
    elif len(nombre)<=1:
        raise ValueError("el nombre esta incompleto")
    else:
        print(f"bienvenido al master en python {nombre}!!")
    
except ValueError:
    print("introduce los datos correctamente")
except Exception as e:
    print("existe un error")