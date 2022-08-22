from coche import Coche

carro1=Coche("Amarillo","Renault","Clio",150,200,4)
carro2=Coche("Rojo","fiat","mobi",150,200,4)
carro3=Coche("Azul","Suzuki","Vitara",150,200,4)
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#detectar el tipo de objeto

#carro3=124 le cambio el tipo apra verificar

if type(carro3)==Coche:
    print("es un objeto correcto")
else:
    print("no es un objeto")