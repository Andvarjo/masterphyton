from usuarios import usuario as modelo
import notas.acciones
class Acciones:
    
    def registro(self):
        print("\nOk vamos a hacer el registro! ")
        nombre=input("Cual es tu nombre? " )
        apellidos=input("Cual es tu Apellido ? " )
        email=input("Cual es tu E-Mail ? " )
        password=input("Cual es tu Password ? " )
        
        usuario=modelo.Usuario(nombre,apellidos,email,password)
        
        registro=usuario.registrar()
        
        if registro[0]>=1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nno te has registrado correctamente")
    
    
    def login(self):
        
        print("\nIdentificate en el sistema: ")
        
        try:
            email=input("Cual es tu E-Mail ? " )
            password=input("Cual es tu Password ? " )
            
            usuario=modelo.Usuario("","",email,password)
            log=usuario.identificar()
            if email==log[3]:
                print(f"\nBienvenido {log[3]} te has identificado en el {log[5] }")
                self.proximasAcciones(log)
        except Exception as error:
            print(type(error))
            print(type(error).__name__)
            print("Login incorrecto, intentalo mas tarde")
    
    
    def proximasAcciones(self,usuario):
        print("""
              Acciones Disponibles:
              -Crear Nota (crear)
              -Mostrar Notas (mostrar)
              -Eliminar Nota (eliminar)
              -Salir (salir)
              """)
        accion=input("Que queires hacer?: ")
        hazEl=notas.acciones.Acciones()
        
        if accion=="crear":
            hazEl.crear(usuario)
            
            self.proximasAcciones(usuario)
        
        elif accion== "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion== "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion== "salir":
            print("hasta la proxima")
            exit()
        
