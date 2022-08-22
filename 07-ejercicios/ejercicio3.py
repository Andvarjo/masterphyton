#imprimir cuadrado de los primeros 60 numeros naturales con while y con for

contador=1

while contador <= 60:
     cuadrado=contador*contador
     print(f"el cuadrado del numero : {contador} es igual a {cuadrado}")
     contador+=1
contador=1
for contador in range(1,61):
    cuadrado=contador*contador
    print(f"el cuadrado del numero : {contador} es igual a {cuadrado}")
 