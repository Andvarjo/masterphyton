#mostar numeros impares entre dos numeros que elija el usuario

numero1=int(input("elija el primer numero: "))
numero2=int(input("elija el segundo numero: "))

rango=numero1-numero2
if rango <1:
    rango=rango*-1
    menor=1
else:
    rango=rango
    menor=0


if menor==1:
    contador=numero1
    while contador<=numero2:
        if contador%2!=0:
            print(contador)
        contador+=1
else:
    contador=numero2
    while contador<=numero1:
        if contador%2!=0:
            print(contador)
        contador+=1