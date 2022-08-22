#programacion orientada a objetos (POO o OOP)

#Definir una clase(molde para crear mas objetos de ese tipo)
#(coche) con caracteristicas similares

from importlib.util import module_for_loader


class Coche:
    
    #atributos o propiedades (variables)
    #caracteristicas del coche
    color="rojo"
    marca="ferrari"
    modelo="aventador"
    velocidad=300
    caballaje=500
    plazas=2
    
    #Metodos, son acciones que hace el objeto (coche)(funciones)
    
    def acelerar(self):
        self.velocidad += 1
        
    def frenar(self):
        self.velocidad-=1
        
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self,color):
        self.color=color
        
    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo=modelo    
        
    def getModelo(self):
        return self.modelo
    
    def setMarca(self,marca):
        self.marca=marca
        
    def getMarca(self):
        return self.marca
    
    



# fin definicion clase

# crear objetos /instanciar la clase

coche=Coche()

print(coche.marca, coche.color, coche.caballaje)
print("Velcoidad actual: ", coche.velocidad, "Km/h")
coche.acelerar()
coche.acelerar()
coche.acelerar()    
coche.acelerar()    
print("Velcoidad nueva: ", coche.velocidad, "Km/h")
coche.frenar()
print("Velcoidad nueva: ", coche.velocidad, "Km/h")



#getter y setter

print("Velcoidad nueva: ", coche.getVelocidad(), "Km/h")
print("color del coche:", coche.getColor())
coche.setColor("amarillo")
print("color del coche:", coche.getColor())
           
    
################## multiples objetos

coche2=Coche()
coche2.setColor("verde")
coche2.setModelo("Gallardo")
print("--------coche 1: ")
print(coche.getColor(),coche.getModelo(),coche.getMarca())

print("--------coche 2: ")
print(coche2.getColor(),coche2.getModelo(),coche2.getMarca())
