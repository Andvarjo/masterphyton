import notas.nota as modelo


class Acciones:
    
    def crear(self,usuario):
        print(f"\n{usuario[1]} vamos a crear una nueva nota..")
        titulo=input("introduce el titulo de tu nota: ")
        descripcion=input("introduce el contenido de tu nota: ")
        nota=modelo.Nota(usuario[0],titulo,descripcion)
        guardar=nota.guardar()
         
        if guardar[0]>=1:
            print(f"\n Perfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\n No se ha guardado la nota {usuario[1]}")
    
    def mostrar(self,usuario):
        print(f"\n Vale {usuario[1]} aqui tienes tus notas : ")
        nota=modelo.Nota(usuario[0])
        notas=nota.listar()
        
        for nota in notas:
            print("\n****************************")
            print(f"TITULO: {nota[2]}")
            print(f"Descripcion: {nota[3]}")
            print("\n****************************")
    
    def borrar(self,usuario):
        print(f"\n OK {usuario[1]} vamos a borrar notas ")
        titulo=input("introduce el titulo de la nota a borrar: ")
        nota= modelo.Nota(usuario[0], titulo)
        eliminar=nota.eliminar()
        
        if eliminar[0]>=1:
            print(f" hemos borrado la nota {nota.titulo}")
        else:
            print("No se ha borrado la nota, prueba luego")