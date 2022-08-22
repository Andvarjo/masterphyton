#crear un script que muestre numero pares del 1 hasta el 120

num=120
contador=0

while contador <= 120:
     
    resto=contador % 2
    if resto==0:
        if  contador!=0:
         print(contador)
    contador+=1
