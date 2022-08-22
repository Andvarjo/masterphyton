

#### mostrar nuemro del 1-100 ####
contador=1
while contador <= 100:
    print(f"estoy en el numero {contador}")
    contador+=1



#### mostar numeros del 0-100 separados por coma en un string#####
contador=1
x=str(0)
while contador <=100:
    x= x + "," + str(contador)
    contador+=1
print(x)    


###### tabla de multiplicar con el While########

numero=int(input("ingresa un numero: "))
if numero <1:
    numero=1

print(f"tabla de multiplicar del: {numero}  ")

contador=1
while contador <=10:
    print(f"{numero} x {contador} = {numero * contador }")
    contador+=1
else:                   # tambien se puede usar else para hacer accion cuando termine el bucle
    print("tabla terminada")




